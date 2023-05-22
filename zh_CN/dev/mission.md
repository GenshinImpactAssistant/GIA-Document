# Mission(自定义任务)


## 介绍


Mission(自定义任务)是GIA中在大世界执行功能的便携集成化单元，使用统一的接口，编写简单，使用方便。

自定义任务可以实现的功能包括行走、采集、战斗、NPC对话(半成品)。通过功能的组合可以实现固定路线采集、任务自动化等功能。

自定义任务是GIA目前添加新功能的重要方向。更精准的自动采集和自动委托都依赖于Mission。

# 设计你的第一个Mission(快速开始)


目前，简单的Mission主要用于自动采集。因此，下面我们介绍一个简单Mission的编写以开始。创建更复杂的Mission可以参阅之后的介绍。

你需要一丁点最基本的python知识以开始。如果你对使用python一无所知，参考[vscode&anaconda python 简单教程](./vscode_python.md)

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

你可以在`missions/MissionQingXin1.py`中找到源代码。

这一段代码的目标是告诉GIA使用`TLPP_FILE`字典中的TLPP(TianLiPositioningPath)文件，沿着该TLPP文件行走并采集沿途的清心。有关如何获得TLPP文件，请参阅[TLPP Video to Path](./video2path.md)

我们将从这一段代码开始，介绍Mission的各个组成部分。

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
VERSION用于标出该Mission的版本。目前(2023.5.20~)使用`1.0.0`进行标记。Mission格式可能会发生修改，若有，将会在文档中说明。
Mission META使用python的字典格式。你可能需要先了解什么是python的字典。

对于快速开始，我们只需
- 复制上面的代码
- 将`your-mission-name-in-zh_CN`改为你的Mission的中文名称，将`your-mission-name-in-en_US`改为你的Mission的英文名称。
- 将`your-github-username`改为你的Github用户名(或者你的任意其他名称)
- 将`when-you-create-the-mission`改为你创建这个Mission的时间(格式：`UTCxxx yyyy-mm-dd`. 例如：`UTC+08 2023-05-03`)
- 将`what-you-want-to-say`改为你想要说的话(路径位置、说明、鸣谢等)

如果META中缺少name或缺少对应语言，则会自动使用mission名。

## 创建Mission类

和示例一样，输入`class MissionMain(MissionJustCollect):`来创建你的Mission类。


## 创建init函数
和示例一样，对于采集自定义任务，使用
```python
    def __init__(self):
        super().__init__(TLPP_FILE, "your-mission-name")

TLPP_FILE = ...
```
就可以创建init函数。


其中，TLPP_FILE是你的TLPP字典, 将V2P中得到的TLPP字典替换`...`。

`your-mission-name`是你的Mission名。

mission的命名规则如下：

1. mission必须为英文
2. mission各个单词的英文首字母应当大写
3. mission应当以你的作者名开头以防止混淆(最好是Github用户名)。GIA自带的Mission没有作者名。

只需指定你要运行的TLPP文件，MissionJustCollect会将它扩展为完整Mission，并调用MissionTemplate类来执行它。

## 将Mission加入GIA

目前，我们就完成了一个Mission的创建。

回顾一下它的样子：

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

1. 把你创建的`your-mission-name.py`文件放置到`./missions`目录下
2. 打开GIA GUI，在`自定义任务配置`页面，点击`编译自定义任务`按钮，完成后按照提示重启GIA
3. 你现在应该可以在重启后的GIA中看到你的Mission了。按照使用一般Mission的方法使用它。

## 结束

到这里，你应该成功创建并运行了你的第一个采集类自定义任务。

欢迎分享你的自定义任务.如果你能够制作自定义任务共享网站,欢迎提交pr或在issue中回复.

> 如果你在阅读`快速开始`文档时，遇到混淆、阻碍或错误，请联系我们或提交issue反馈。

# Mission详细介绍

这是面向有一定python基础的开发者。


从MissionExecutor类继承。

## 方法


MissionExecutor有以下方法：

1.  move(MODE:str = None,
1.  move(MODE:str = None,
    stop_rule:int = None,
    target_posi:list = None,
    path_dict:dict = None,
    to_next_posi_offset:float = None,
    special_keys_posi_offset:float = None,
    reaction_to_enemy:str = None,
    is_tp:bool=None)
1.  move(MODE:str = None,
    stop_rule:int = None,
    target_posi:list = None,
    path_dict:dict = None,
    to_next_posi_offset:float = None,
    special_keys_posi_offset:float = None,
    reaction_to_enemy:str = None,
    is_tp:bool=None)
1.  move(MODE:str = None,
    stop_rule:int = None,
    target_posi:list = None,
    path_dict:dict = None,
    to_next_posi_offset:float = None,
    special_keys_posi_offset:float = None,
    reaction_to_enemy:str = None,
    is_tp:bool=None)
1.  move(MODE:str = None,
    stop_rule:int = None,
    target_posi:list = None,
    path_dict:dict = None,
    to_next_posi_offset:float = None,
    special_keys_posi_offset:float = None,
    reaction_to_enemy:str = None,
    is_tp:bool=None)
1.  move(MODE:str = None,
    stop_rule:int = None,
    target_posi:list = None,
    path_dict:dict = None,
    to_next_posi_offset:float = None,
    special_keys_posi_offset:float = None,
    reaction_to_enemy:str = None,
    is_tp:bool=None)
1.  move(MODE:str = None,
    stop_rule:int = None,
    target_posi:list = None,
    path_dict:dict = None,
    to_next_posi_offset:float = None,
    special_keys_posi_offset:float = None,
    reaction_to_enemy:str = None,
    is_tp:bool=None)
1.  move(MODE:str = None,
    stop_rule:int = None,
    target_posi:list = None,
    path_dict:dict = None,
    to_next_posi_offset:float = None,
    special_keys_posi_offset:float = None,
    reaction_to_enemy:str = None,
    is_tp:bool=None)

MODE: 移动模式。有以下两种：

AUTO：朝着target_posi直线行走。
PATH：按照TeyvatMovePath行走。

默认为AUTO。

stop_rule：停止条件。有以下两种：

0：到达目标停止。
1：识别到F停止。

默认为0。

target_posi：目标坐标。使用AUTO模式时填写。按照TIanLi坐标格式。

path_dict：TeyvatMovePath格式文件。使用PATH模式时传入。

is_tp：是否在移动前传送。默认为False。

其他参数为offset或待实现参数。

2. move_straight(self, position, is_tp = False)

position同target_posi。简化版的move。

3. move_along(self, path, is_tp = False)

path：填写TMP格式文件。仅需填写文件名，不用后缀。

4. combat()

打一架。打完就润。

5. collect(self, MODE = None,
5. collect(self, MODE = None,
                collection_name =  None,
                collector_type =  None,
                is_combat =  None,
                is_activate_pickup = None,
                pickup_points = None
                )
5. collect(self, MODE = None,
                collection_name =  None,
                collector_type =  None,
                is_combat =  None,
                is_activate_pickup = None,
                pickup_points = None
                )
5. collect(self, MODE = None,
                collection_name =  None,
                collector_type =  None,
                is_combat =  None,
                is_activate_pickup = None,
                pickup_points = None
                )
5. collect(self, MODE = None,
                collection_name =  None,
                collector_type =  None,
                is_combat =  None,
                is_activate_pickup = None,
                pickup_points = None
                )
5. collect(self, MODE = None,
                collection_name =  None,
                collector_type =  None,
                is_combat =  None,
                is_activate_pickup = None,
                pickup_points = None
                )
5. collect(self, MODE = None,
                collection_name =  None,
                collector_type =  None,
                is_combat =  None,
                is_activate_pickup = None,
                pickup_points = None
                )

MODE：没什么用。

collection_name: 采集物名称。可留空。

collector_type: 采集物类型。可留空。默认为COLLECTION。

is_combat: 是否战斗。

is_activate_pickup: 是否主动采集。

pickup_points: 是否在指定坐标拾取。若是，则填入坐标，否则留空。

该方法的执行顺序为：战斗->在指定坐标采集->在范围内搜索采集。若在任意阶段搜索到敌人，则会重新进入战斗状态。指定坐标采集不会重复。

6. start_pickup()

开始识别并采集。调用该方法后，会在之后的过程中使用pickup_operator自动识别F键采集。

7. stop_pickup()

停止识别并采集。

## 写一个Mission


首先，继承MissionExecutor。

```python
from source.mission.mission_template import MissionExecutor

class MissionMain(MissionExecutor):
    def __init__(self):
        super().__init__()
        self.setName("MissionTest")
```
注意，类名必须为MissionMain。使用首字母大写命名格式。

然后，实现exec_mission方法。

```python
    def exec_mission(self):
        self.move_along("167858534153", is_tp=True)
        self.collect(MODE="AUTO",pickup_points=[[71, -2205],[65,-2230]])
```

这是一个示例。

最后，如果你要调试你的mission，在下方加入以下代码：

```python
if __name__ == '__main__':
    mission = MissionTest()
    mission.start()
    mission.continue_threading()
```

运行该文件即可。

## 添加你的Mission


同上

