# Mission（自定义任务）

## Introduction

Mission is a portable, integrated unit in GIA that performs functions in the Teyvat world, using a unified interface that is simple to write and use.

Mission can achieve the functions of gathering, combat, NPC dialogue (crafting) and walking. The combination of functions allows for fixed route gathering, mission automation and more.

Custom task is an important direction for GIA to add new functions at present.

# 设计你的第一个Mission（快速开始） - 从GUI界面创建

GIA 1.2.0版本之后，你可以从GUI中轻松完成自定义任务的创建。

参考[在GUI中创建自定义任务](../create_mission_in_GUI.md)

# 从代码创建

Currently, simple Missions are mainly used for automatic collection. Therefore, below we introduce the writing of a simple Mission to start. To create more complex Missions, please refer to the introduction later.

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

这一段代码的目标是告诉GIA使用 `TLPP_FILE` 字典中的TLPP(TianLiPositioningPath)文件，沿着该TLPP文件行走并采集沿途的清心。

有关如何获得TLPP文件，请参阅：

- [TLPP Record Path](../record_path.md)(易于上手)
- [TLPP Video to Path](video2path.md)

We will start with this piece of code and introduce the various components of Mission.

## 导入Mission模板

对于简单的采集自定义任务，应当使用：

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

For a quick start, we simply:

- Copy the above code.
- Change `your-mission-name-in-zh_CN` to the Chinese name of your Mission, and `your-mission-name-in-en_US` to the English name of your Mission.
- Change `your-github-username` to your Github username (or whatever you want).
- Change `when-you-create-the-mission` to the time when you created this Mission (format: `UTCxxx yyyy-mm-dd` . For example: `UTC+08 2023-05-03` ).
- Change `what-you-want-to-say` to what you want to say (path location, description, acknowledgments, etc.).

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

其中，TLPP_FILE是你的TLPP字典, 将V2P中得到的TLPP字典直接复制粘贴到python文件中。

`your-mission-name` is your Mission name.

mission的命名规则如下：

1. The mission must be in English.
2. The first letter of each word of mission should be capitalized.
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

1. 把你创建的 `your-mission-name.py` 文件放置到 `./local_edit_missions` 目录下
2. 打开GIA GUI，打开 `自定义任务配置` 页面
3. 你现在应该可以在重启后的GIA中看到你的Mission了。本地的自定义任务将会加粗显示。按照使用一般Mission的方法使用它。

- 注：目前，只有将自定义任务PR到[仓库](https://github.com/GenshinImpactAssistant/GIA-Missions)，通过下载的方式才能显示meta信息。

## 结束

到这里，你应该成功创建并运行了你的第一个采集类自定义任务。

非常欢迎分享你的自定义任务。如果你愿意分享，请查看 https://github.com/GenshinImpactAssistant/GIA-Missions

> If you encounter confusion, obstacles or errors while reading the `quickstart` documentation, please contact us or submit an issue feedback.

# Mission详细介绍

这是面向有一定python基础的开发者。

You need to understand the basic syntax of python, but you don't need to master it.

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

You can check the method and introduction at [`source/mission/mission.py`](https://github.com/infstellar/genshin_impact_assistant/blob/main/source/mission/mission.py). Please submit an issue if the documentation is not clear or if you want to add new features to suit your ideas.

List of functions:

| 函数                          | 用途                                                                                                                 |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| move_straight                 | 向目的地前进                                                                                                         |
| move_along                    | 沿着TLPP行走                                                                                                         |
| start_combat                  | 开始战斗                                                                                                             |
| stop_combat                   | 停止战斗                                                                                                             |
| pickup_once                   | 拾取1次                                                                                                              |
| collect                       | 启动收集                                                                                                             |
| circle_search                 | 进入一个循环，以中心坐标为圆心向外移动搜索。当符合stop_rule时退出                                                    |
| start_pickup                  | 启动自动采集。会采集路上遇到的可交互物品。                                                                           |
| stop_pickup                   | 停止自动采集。                                                                                                       |
| refresh_picked_list           | 刷新已采集物名列表                                                                                                   |
| reg_exception_found_enemy     | 注册事件：条件：是否遇敌。此后条件成立则跳出阻塞式任务。                                                             |
| reg_exception_chara_died      | 注册事件：条件：角色是否死亡。此后条件成立则跳出阻塞式任务。                                                         |
| reg_exception_low_hp          | 注册事件：条件：检测角色是否低血量。此后条件成立则跳出阻塞式任务。                                                   |
| set_default_arrival_mode      | Set the default accurate arrival mode. The default exact reach mode for all move methods henceforth is set to state. |
| reg_fight_if_needed           | 注册事件：设置是否遇到可见的敌人就开战。设置为state。                                                                |
| set_raise_exception           | 设置是否遇到异常时抛出异常并强制退出任务。设置为state。                                                              |
| set_exception_mode            | 设置阻塞式任务遇到异常时的默认处理方式。                                                                             |
| set_puo_crazy_f               | 设置是否启用疯狂按f模式。启用后，puo将会在按下f拾取后不停按f若干次。                                                 |
| handle_tmf_stuck_then_skip    | 传入TMF的错误码，如果出错则跳过。                                                                                    |
| handle_tmf_stuck_then_recover | 传入TMF的错误码，如果出错则到七天神像回血。                                                                          |
| handle_tmf_stuck_then_raise   | 传入TMF的错误码，如果出错则抛出异常，退出任务。                                                                      |
| switch_character_to           | 切换角色到指定角色。角色名为英文。                                                                                   |
| use_f                         | 按一下f。                                                                                                            |
| is_combat_end                 | 战斗是否结束。你可以在while循环中判断它。                                                                            |

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
