# genshin_impact_assistant 原神助手

<div align="center">

基于图像识别和模拟按键的多功能原神自动辅助操作,包括自动战斗,自动刷秘境,自动刷大世界材料。

GIA的目标是：让程序负责玩原神，你负责抽卡和带着角色逛街~~养老婆~~

[![GitHub Star](https://img.shields.io/github/stars/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/stargazers)
[![Release Download](https://img.shields.io/github/downloads/infstellar/genshin_impact_assistant/total?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/releases/download/v0.3.0/GIA.Launcher.v0.3.0.7z)
[![Release Version](https://img.shields.io/github/v/release/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/releases/latest)
[![Python Version](https://img.shields.io/badge/python-v3.7.6-blue?style=flat-square)](https://www.python.org/downloads/release/python-376/)
[![GitHub Repo Languages](https://img.shields.io/github/languages/top/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/search?l=Python)
![GitHub Repo size](https://img.shields.io/github/repo-size/infstellar/genshin_impact_assistant?style=flat-square&color=3cb371)
[![contributors](https://img.shields.io/github/contributors/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/graphs/contributors)
</br></br>
[![QQ群](https://img.shields.io/badge/QQ群-901372518-blue.svg?style=flat-square&color=12b7f5&logo=qq)](https://jq.qq.com/?_wv=1027&k=YLTrqlzX)
[![Bilibili](https://img.shields.io/badge/bilibili-infstellar-blue.svg?style=flat-square&logo=bilibili)](https://space.bilibili.com/313212782)<!-- ignore gettext -->

</div>

# 介绍


基于图像识别的原神自动操作辅助.使用图片识别与模拟键盘操作,不涉及违规操作.

To没用过github的小伙伴: 描述文档中的蓝色文字是链接,可以打开的.

## 演示视频


<https://www.bilibili.com/video/BV1RV4y157m6>(挂了)

补档 <https://www.youtube.com/watch?v=ZieBDx6Go4A> v0.2.0的演示视频，可能部分过期

## 功能介绍


### 1. [自动战斗辅助](./combat_assi.md)


- 在GUI中将FlowMode切换到AutoCombat，等待模块导入

- 按下`[`键启动/停止功能。可在`keymap.json`中更改。

其他设置参见[自动战斗辅助介绍](./combat_assi.md).

### 2. [自动秘境辅助](./domain_assi.md)


1. 在config中设置挑战秘境的次数与其他设置,详见[config设置](./config.md).
2. 手动选择队伍,配置队伍,进入秘境.
3. 进入秘境后(也可以在大世界),在GUI TaskList中选中DomainTask，点击启动任务
4. 等待导入完成后切换到原神

- 注意阅读[domain_assi.md](./domain_assi.md)中的注意事项.

其他设置参见[自动秘境辅助介绍](./domain_assi.md).

### 3. [自动采集辅助](./collector_assi.md)


演示视频：<https://www.bilibili.com/video/BV163411Q7fD>

- 在GUI中将Mission Group切换到AutoCollectorMission.json

- 选中Task List -> Mission，启动Task

- 注意阅读[collector_assi.md](./collector_assi.md)中的注意事项.

其他设置参见[自动采集辅助介绍](./collector_assi.md).

### 4. [自动每日委托辅助](./commission_assi.md)

**正在早期测试，请谨慎开启并汇报遇到的错误。**

> 目前仅能完成以下委托：ASmallStepForHilichurls,Emergency,IcyIssues,ForTheHarbingers,BigIceColdCrisis,SpreadingEvil,PudgyPyrotechnicians,IncreasingDanger.

详情参见[自动每日委托辅助介绍](./commission_assi.md).

### 5. [每日领取凯瑟琳](./claim_reward.md)

参见[领取日常奖励](./commission_assi.md).

### 6. [自动地脉衍出辅助](./ley_line_ourcrop.md)

参见[自动地脉衍出辅助介绍](./ley_line_ourcrop.md).

## 使用方法


### 快速安装


请参见[GIA Launcher自动安装器使用方法](install.md).

### 从源代码构建


请参见[源代码安装方法](git_install.md)

## 使用前设置


### 原神窗口设置


- 需要在原神启动后再运行程序.

- 原神需要以1080p窗口化运行(全屏也可以),设置抗锯齿为SMAA,中或以上特效.

- 窗口焦点应在原神窗口上。如果切换焦点窗口，程序会暂停所有键鼠操作并等待。

### config配置


在使用前，需要注意这些配置内容：

|位置|配置项|内容|
|----|----|----|
|config/settings/config.json| `BorderlessWindow` | 如果是无边框窗口或全屏，设置为true。|

可以在GUI或直接从文件中修改。

更多其他配置项，参见GUI内的设置介绍。

### GUI使用


#### main窗口


- 点击main按钮进入
- Task List：选择要执行的任务，只能从GUI里启动
- FlowMode：选择当前启用的功能，只能按快捷键启动
- Mission: 选择要启动的任务组，然后在Task List选中Mission，启动Task List
- Log：输出日志

#### 设置页面


- 点击按钮进入

- 在下拉列表中选择对应的项目，进行配置。

远程操作等更多GUI使用方法，参考[GUI使用](./gui.md)

### 自动战斗，自动采集设置窗口


- 点击对应按钮进入，按照提示操作

## 错误报告


如果在使用中遇到问题，可以提交issue或在Q群中反馈。

反馈错误前，请务必确认您已经阅读文档和[FAQ](FAQ.md)中的已知问题与解决方案。

反馈错误时，请一并提交 Logs 文件夹中的日志文件。

## 错误码


如果日志输出了`ERR_CODE`或`WARN_CODE`，可以在[ERROR_CODE](error_code.md)中查看对应的信息：


如果在使用时遇到问题，可以先看看FAQ：

[FAQ](FAQ.md)

## 已知问题 Known Issues


[Known issues](known_issues.md)

## 性能需求


- 此程序至少需要`2.5G内存`与`3G存储空间`(完整安装).

## 鸣谢


### 特别感谢


- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript)

### 开源库


#### 原神相关


- [原神-基于图像算法的坐标定位 GenshinImpact AutoTrack DLL](https://github.com/GengGode/cvAutoTrack)

- [空荧酒馆原神地图 kongying-tavern/yuan-shen-map](https://github.com/kongying-tavern/yuan-shen-map)

- [原神英語・中国語辞典 xicri/genshin-dictionary](https://github.com/xicri/genshin-dictionary)

#### 开源库调用


- [opencv](https://github.com/opencv/opencv)
- [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)
- [yolox](https://github.com/Megvii-BaseDetection/YOLOX)
- [pyinstaller](https://github.com/pyinstaller/pyinstaller)

#### 其他


- [GIS 参考了自动战斗脚本的格式](https://github.com/phonowell/genshin-impact-script)

### 其他贡献/参与者


- 数据集标注: [nɡ.](https://space.bilibili.com/396023811)

