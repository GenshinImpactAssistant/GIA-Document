# Mission(自定义任务)

## Introduction

Mission is a portable, integrated unit in GIA that performs functions in the Teyvat world, using a unified interface that is simple to write and use.

Mission can achieve the functions of gathering, combat, NPC dialogue (crafting) and walking. The combination of functions allows for fixed route gathering, mission automation and more.

Custom task is an important direction for GIA to add new functions at present.

# 设计你的第一个Mission(快速开始)

At present, the simple Mission is mainly used for automatic collection.

You need a minimal knowledge of python to get started.

## 示例

这是一个最简单的Mission代码：

```python
from source.mission.template.mission_just_collect import MissionJustCollect
VERSION='1.0.0'
META={
    'name':{
        'zh_CN':'采集清心1',
        'en_US':'Collect Qing xin 1'
    }
}

class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(TLPP_FILE, "MissionQingXin1")

TLPP_FILE = ...
```

You can find the source code in `missions/MissionQingXin1.py`.

这一段代码的目标是告诉GIA使用 `TLPP_FILE` 字典中的TLPP(TianLiPositioningPath)文件，沿着该TLPP文件行走并采集沿途的清心。有关如何获得TLPP文件，请参阅[TLPP Video to Path](video2path.md)

We will start with this piece of code and introduce the various components of Mission.

## 导入Mission模板

对于简单的采集自定义任务，应当使用

```python
from source.mission.template.mission_just_collect import MissionJustCollect
```

导入MissionJustCollect模板类。

## 创建Mission信息

在导入模板类之后，输入以下代码：

```python
VERSION='1.0.0'
META={
    'name':{
        'zh_CN':'your-mission-name-in-zh_CN',
        'en_US':'your-mission-name-in-en_US'
    },
    'author':'your-github-account-name',
    'time':'when-you-create-the-mission',
    'note':'what-you-want-to-say'
}
```

VERSION用于标出该Mission的版本。目前(2023.5.20~)使用 `1.0.0` 进行标记。Mission格式可能会发生修改，若有，将会在文档中说明。Mission META使用python的字典格式。你可能需要先了解什么是python的字典。

For a quick start, we simply

- Copy the above code
- Change `your-mission-name-in-zh_CN` to the Chinese name of your Mission, and `your-mission-name-in-en_US` to the English name of your Mission.
- Change `your-github-username` to your Github username (or whatever you want)
- Change `when-you-create-the-mission` to the time when you created this Mission (format: `UTCxxx yyyy-mm-dd` . For example: `UTC 08 2023-05-03` )
- Change `what-you-want-to-say` to what you want to say (path location, description, acknowledgments, etc.)

If the name or corresponding language is missing in META, the mission name will be used automatically.

## 创建Mission类

和示例一样，输入 `class MissionMain(MissionJustCollect):` 来创建你的Mission类。

## 创建init函数

和示例一样，对于采集自定义任务，使用

```python
    def __init__(self):
        super().__init__(TLPP_FILE, "your-mission-name")

TLPP_FILE = ...
```

就可以创建init函数。

Among them, TLPP_FILE is your TLPP dictionary, replace `...` with the TLPP dictionary obtained in V2P.

`your-mission-name` is your Mission name.

mission的命名规则如下：

1. The mission must be in English
2. The first letter of each word of mission should be capitalized
3. mission should start with your author name to prevent confusion (preferably Github username).

Just specify the TLPP file you want to run, MissionJustCollect will expand it into a complete Mission, and call the MissionTemplate class to execute it.

## 将Mission加入GIA

目前，我们就完成了一个Mission的创建。

Here's a look back at what it looks like:

```python
from source.mission.template.mission_just_collect import MissionJustCollect
META={
    'name':{
        'zh_CN':'your-mission-name-in-zh_CN',
        'en_US':'your-mission-name-in-en_US'
    }
}
class MissionMain(MissionJustCollect):
    def __init__(self):
        super().__init__(TLPP_FILE, "your-mission-name")

TLPP_FILE = ...
```

要使用这个Mission，我们需要将它加入GIA的Mission Index来让GIA识别这个mission。方法如下：

1. Place the `your-mission-name.py` file you created in the `./missions` directory
2. Open the GIA GUI, click the `Compile Custom Task` button on the `Custom Task Configuration` page, and restart GIA according to the prompts after completion
3. You should now be able to see your Mission in the restarted GIA.

## 结束

到这里，你应该成功创建并运行了你的第一个采集类自定义任务。

非常欢迎分享你的自定义任务.

If you can make a custom task sharing website, welcome to submit pr or reply in issue.

> If you encounter confusion, obstacles or errors while reading the `quickstart` documentation, please contact us or submit an issue feedback.

# Mission详细介绍

这是面向有一定python基础的开发者。

You need to master the basic syntax of python.

## Usage

Inherited from the MissionExecutor class.

```python
from source.mission.mission import Mission
class MissionMain(Mission): ...
```

## Methods

You can check the method and introduction at [`source/mission/mission.py`](https://github.com/infstellar/genshin_impact_assistant/blob/main/source/mission/mission.py).

## Write a Mission

First, inherit Mission.

```python
from source.mission.mission import Mission

class MissionMain(Mission):
    def __init__(self):
        super().__init__()
        self.setName("MissionTest")
```

Note that the class name must be MissionMain.

Then, implement the exec_mission method.

```python
    def exec_mission(self):
        self.move_along(TLPP_DICT, is_tp=True)
        self.collect(MODE="AUTO",pickup_points=[[71, -2205],[65,-2230]])
```

Here is an example.

Your program must be written in the exec_mission function to be executed. The same is true for commission.

Finally, if you want to debug your mission, add the following code below:

```python
if __name__ == '__main__':
    mission = MissionMain()
    mission.start()
    mission.continue_threading()
```

Just run the file.

You can perform functions by combining functions. For the functions provided by mission, please refer to the function documentation below.

## 函数文档

你可以在[ `source/mission/mission.py` ](https://github.com/infstellar/genshin_impact_assistant/blob/main/source/mission/mission.py)查看所有使用方法和介绍. 如果文档不清晰或想要添加新的功能以适配你的想法,请提交issue.

Function list:

| function                      | purpose                                                                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| move_straight                 | move towards the destination                                                                                                              |
| move_along                    | Walk along TLPP                                                                                                                           |
| start_combat                  | Start Combat                                                                                                                              |
| stop_combat                   | stop combat                                                                                                                               |
| pickup_once                   | Pick up 1 time                                                                                                                            |
| collect                       | start collection                                                                                                                          |
| circle_search                 | Enter a loop, and search outward with the center coordinates as the center of the circle. Exit when stop_rule is met.                     |
| start_pickup                  | Start automatic pickup. Interactable items encountered on the road will be collected.                                                     |
| stop_pickup                   | Stop automatic pickup.                                                                                                                    |
| refresh_picked_list           | Refresh the list of picked items                                                                                                          |
| reg_exception_found_enemy     | Register event: Condition: Enemy found or not. After that, if the condition is met, it will jump out of the blocking task.                |
| reg_exception_chara_died      | Register event: Condition: Whether the character died. After that, if the condition is met, it will jump out of the blocking task.        |
| reg_exception_low_hp          | Register event: Condition: Check if the character has low HP. After that, if the condition is met, it will jump out of the blocking task. |
| set_default_arrival_mode      | Set the default accurate arrival mode. The default exact reach mode for all move methods henceforth is set to state.                      |
| reg_fight_if_needed           | Register event: set whether to start a fight when encountering a visible enemy. Set to state.                                             |
| set_raise_exception           | Sets whether an exception is thrown and the task is forced to exit when an exception is encountered. Set to state.                        |
| set_exception_mode            | Set the default processing mode when a blocking task encounters an exception.                                                             |
| set_puo_crazy_f               | Set whether to enable the crazy pressing f mode. After enabling, puo will keep pressing f several times after pressing f to pick up.      |
| handle_tmf_stuck_then_skip    | The error code passed in to TMF, if there is an error, it will be skipped.                                                                |
| handle_tmf_stuck_then_recover | Pass in the error code of TMF, if there is an error, it will return blood from the statue.                                                |
| handle_tmf_stuck_then_raise   | Pass in the error code of TMF, if there is an error, throw an exception and exit the task.                                                |
| switch_character_to           | Switch character to specified character.                                                                                                  |
| use_f                         | Press f.                                                                                                                                  |
| is_combat_end                 | Whether the combat is over. You can judge it in the while loop.                                                                           |

## 示例

You can find some examples in `source/mission/missions`, `source/commission/commissions`.

Example 1: Concrete implementation of the MissionJustCollect class.

```python
class MissionJustCollect(Mission):
    def __init__(self, dictname, name):
        super().__init__(is_CFCF=True,is_PUO=True,is_TMCF=True)
        self.dictname = dictname
        self.setName(name)
  

    def exec_mission(self):
        self.start_pickup()
        self.move_along(self.dictname, is_tp=True, is_precise_arrival=False)
        self.stop_pickup()
```

Example 2: Survey point collection template

```python
class MissionMain(Mission):
    def __init__(self):
        super().__init__()
  

    def exec_mission(self):
        self.set_puo_crazy_f(True)
        self.start_pickup()
        self.move_along(TLPP_FILE, is_tp=True, is_precise_arrival=False)
        self.stop_pickup()
```

## 添加你的Mission

同上
