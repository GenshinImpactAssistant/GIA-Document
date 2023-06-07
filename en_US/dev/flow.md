# Flow control Unit

## What is Flow?

Flow can be understood as a state machine. Flow is composed of Flow Unit (Flow Template), and one Flow Unit can be switched to another Flow Unit.

There are 5 states inside the Flow Unit, which can be switched between states.

Through the switching of the Flow Unit and the switching inside the Unit, different states can be switched according to different conditions.

Currently, Flow is used for automatic collection, automatic walking and path recording. You possibly don't need to write a new Flow. It can be understood without the need to master it.

## FlowTemplate

基本流程单元。

### 基本概念：

Flow id: 存储于模块ST。

Flow Code: 存储于模块FC。

```python
class FlowTemplate():
    def __init__(self, upper:FlowConnector, flow_id:int, next_flow_id:int, flow_timeout_time:float = -1):
```

介绍：upper：流程连接器（FlowConnector）单元。

flow_id: 流程代码：

## Flow Code

Taking the automatic secret realm as an example, it has the following process codes:

MOVETO_CHALLENGE

CHALLENGE

GETTING_REAWARD

FINGING_TREE

MOVETO_TREE

ATTAIN_REAWARD

END_DOMAIN

Among them, the termination process code must contain $END$ characters.

All process codes are managed in flow/flow_state.py.

next_flow_id: Flow id of the next process to run after the process ends

flow_timeout_time: Flow timeout time. INF for negative numbers.

Variable:

rfc: return flow code. There are the following 6 values: 0,1,2,3,4,5

0~4: corresponding to state_init, state_before, state_in, state_after, state_end. That is, FC.INIT, FC.BEFORE, FC.IN, FC.AFTER, FC.END.

5: Process end flag code.

### 状态执行函数：

`state_init, state_before, state_in, state_after, state_end.`

其中，state_init与state_end为单次执行函数，即在一个Flow单元中的一次执行中只执行一次。

state_before and state_after can switch back and forth, for example:

```python
def state_after(self):
    ...
    self._set_rfc(FC.BEFORE)
```

switch back to the before state.

state_in is a cyclic state, that is, if some code of the process needs to be executed cyclically, write it here.

Finally, the above rules are only suggestions and standards. If you don’t follow them, you won’t go wrong. They are just for maintenance.

If you don't need a certain state, just don't implement it in the inherited class. However, state_in must be implemented.

After each state is achieved, if you want to switch to the next state, you must use `self._next_rfc()`. Manual `self._set_rfc(x)` is also possible.

List of functions:

| name               | func                                       |
| ------------------ | ------------------------------------------ |
| \_next_rfc()       | Switch to the next FlowCode                |
| \_before_timeout() | Do something before the function times out |
| \_set_nfid()       | Set the next process id                    |

## FlowConnector

流程连接器。

All process variables should be stored here for easy reset and setting.

A FlowController must have one and only one FlowConnector.

## FlowController

流程控制器。

The main program of the process, which controls the flow of the process.

```python
class FlowController(base_threading.BaseThreading):
    def __init__(self, flow_connector:FlowConnector, current_flow_id):
```

flow_connector: FlowConnector object.

current_flow_id: The initial flow id.

List of functions:

| name                  | func                                             |
| --------------------- | ------------------------------------------------ |
| append_flow()         | Add a FlowTemplate to the process execution list |
| \_err_code_exec()     | Error code analysis                              |
| set_current_flow_id() | set flow id                                      |

## EndFlowTemplate

同FlowTemplate。区别是

1. Need to fill in err_code.
2. The process ID must contain `$END$`.
