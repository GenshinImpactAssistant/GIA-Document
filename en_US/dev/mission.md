# Mission(自定义任务)

## Introduction

Mission(自定义任务)是GIA中在大世界执行功能的便携集成化单元，使用统一的接口，编写简单，使用方便。

自定义任务可以实现的功能包括行走、采集、战斗、NPC对话(半成品)。通过功能的组合可以实现固定路线采集、任务自动化等功能。

自定义任务是GIA目前添加新功能的重要方向。更精准的自动采集和自动委托都依赖于Mission。

# 设计你的第一个Mission(快速开始)

目前，简单的Mission主要用于自动采集。因此，下面我们介绍一个简单Mission的编写以开始。创建更复杂的Mission可以参阅之后的介绍。

你需要一丁点最基本的python知识以开始。如果你对使用python一无所知，参考[vscode&anaconda python 简单教程(还没写)](vscode_python.md)

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

你可以在 `missions/MissionQingXin1.py` 中找到源代码。

这一段代码的目标是告诉GIA使用 `TLPP_FILE` 字典中的TLPP(TianLiPositioningPath)文件，沿着该TLPP文件行走并采集沿途的清心。有关如何获得TLPP文件，请参阅[TLPP Video to Path](video2path.md)

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

VERSION用于标出该Mission的版本。目前(2023.5.20~)使用 `1.0.0` 进行标记。Mission格式可能会发生修改，若有，将会在文档中说明。Mission META使用python的字典格式。你可能需要先了解什么是python的字典。

对于快速开始，我们只需

- 复制上面的代码
- 将 `your-mission-name-in-zh_CN` 改为你的Mission的中文名称，将 `your-mission-name-in-en_US` 改为你的Mission的英文名称。
- 将 `your-github-username` 改为你的Github用户名(或者你的任意其他名称)
- 将 `when-you-create-the-mission` 改为你创建这个Mission的时间(格式： `UTCxxx yyyy-mm-dd` . 例如： `UTC+08 2023-05-03` )
- 将 `what-you-want-to-say` 改为你想要说的话(路径位置、说明、鸣谢等)

如果META中缺少name或缺少对应语言，则会自动使用mission名。

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

其中，TLPP_FILE是你的TLPP字典, 将V2P中得到的TLPP字典替换 `...` 。

`your-mission-name` 是你的Mission名。

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

1. 把你创建的 `your-mission-name.py` 文件放置到 `./missions` 目录下
2. 打开GIA GUI，在 `自定义任务配置` 页面，点击 `编译自定义任务` 按钮，完成后按照提示重启GIA
3. 你现在应该可以在重启后的GIA中看到你的Mission了。按照使用一般Mission的方法使用它。

## 结束

到这里，你应该成功创建并运行了你的第一个采集类自定义任务。

非常欢迎分享你的自定义任务.

如果你能够制作自定义任务共享网站,欢迎提交pr或在issue中回复.

> 如果你在阅读 `快速开始` 文档时，遇到混淆、阻碍或错误，请联系我们或提交issue反馈。

# Mission详细介绍

这是面向有一定python基础的开发者。

你需要掌握python的基础语法。(不需要特别高深的python知识)

## Usage

从Mission类继承。

```python
from source.mission.mission import Mission
class MissionMain(Mission): ...
```

## Methods

你可以在 [`source/mission/mission.py` ](https://github.com/infstellar/genshin_impact_assistant/blob/main/source/mission/mission.py)查看方法与介绍。

### Write a Mission

首先，继承Mission。

```python
from source.mission.mission import Mission

class MissionMain(Mission):
    def __init__(self):
        super().__init__()
        self.setName("MissionTest")
```

注意，类名必须为MissionMain。使用首字母大写命名格式。

然后，实现exec_mission方法。

```python
    def exec_mission(self):
        self.move_along(TLPP_DICT, is_tp=True)
        self.collect(MODE="AUTO",pickup_points=[[71, -2205],[65,-2230]])
```

这是一个示例。

你的程序必须写在exec_mission函数中才能被执行. commission同理.

最后，如果你要调试你的mission，在下方加入以下代码：

```python
if __name__ == '__main__':
    mission = MissionMain()
    mission.start()
    mission.continue_threading()
```

运行该文件即可。

你可以通过组合函数以执行功能.有关mission提供的函数,请参阅下方的函数文档.

## 函数文档

你可以在[ `source/mission/mission.py` ](https://github.com/infstellar/genshin_impact_assistant/blob/main/source/mission/mission.py)查看所有使用方法和介绍. 如果文档不清晰或想要添加新的功能以适配你的想法,请提交issue.

函数清单:

| 函数                            | 用途                                    |
| ----------------------------- | ------------------------------------- |
| move_straight                 | 向目的地前进                                |
| move_along                    | 沿着TLPP行走                              |
| start_combat                  | 开始战斗                                  |
| stop_combat                   | 停止战斗                                  |
| pickup_once                   | 拾取1次                                  |
| collect                       | 启动收集                                  |
| circle_search                 | 进入一个循环，以中心坐标为圆心向外移动搜索。当符合stop_rule时退出 |
| start_pickup                  | 启动自动采集。会采集路上遇到的可交互物品。                 |
| stop_pickup                   | 停止自动采集。                               |
| refresh_picked_list           | 刷新已采集物名列表                             |
| reg_exception_found_enemy     | 注册事件：条件:是否遇敌。此后条件成立则跳出阻塞式任务           |
| reg_exception_chara_died      | 注册事件：条件:角色是否死亡。此后条件成立则跳出阻塞式任务。        |
| reg_exception_low_hp          | 注册事件：条件:检测角色是否低血量。此后条件成立则跳出阻塞式任务。     |
| set_default_arrival_mode      | 设置默认精确到达模式。此后所有移动方法的默认精确到达模式设置为state。 |
| reg_fight_if_needed           | 注册事件：设置是否遇到可见的敌人就开战。设置为state。         |
| set_raise_exception           | 设置是否遇到异常时抛出异常并强制退出任务。设置为state。        |
| set_exception_mode            | 设置阻塞式任务遇到异常时的默认处理方式.                  |
| set_puo_crazy_f               | 设置是否启用疯狂按f模式.启用后,puo将会在按下f拾取后不停按f若干次. |
| handle_tmf_stuck_then_skip    | 传入TMF的错误码，如果出错则跳过。                    |
| handle_tmf_stuck_then_recover | 传入TMF的错误码，如果出错则到七天神像回血。               |
| handle_tmf_stuck_then_raise   | 传入TMF的错误码，如果出错则抛出异常，退出任务。             |
| switch_character_to           | 切换角色到指定角色。角色名为英文。                     |
| use_f                         | 按一下f.                                 |
| is_combat_end                 | 战斗是否结束.你可以在while循环中判断它.               |

## 示例

你可以在 `source/mission/missions` , `source/commission/commissions` 中找到一些范例.

示例1: MissionJustCollect类的具体实现.

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

示例2: 调查点采集模板

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
