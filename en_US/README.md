# Genshin Impact Assistant

<div align="center">

A multi-functional auto-assist based on image recognition and keystroke simulation, including auto combat, auto domain and auto claim materials in Teyvat world

The aim of GIA is: let the program play Genshin, and you just need to selected characters and raise them.

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

## Introduction


An Genshin automatic operation assistance based on image recognization and similated keyboard operation. Does not involve not-allowed operation.

To those who have not used github: the blue text in the docs is a hyperlink that can be clicked.

## 我是急急国王


如果你啥都不想看就想开始用，按照[这个方法](./jijiking.md)操作：

## Demo Video


<https://www.youtube.com/watch?v=ZieBDx6Go4A> v0.2.0的演示视频，可能过期

## [常见问题 FAQ](FAQ.md)


如果在使用时遇到问题，先看看[FAQ](FAQ.md)：

[FAQ](FAQ.md)

## Function Introduction


### 1. [战斗辅助](./combat_assi.md)


- Switch Function to AutoCombat and wait for the module to be imported.
- Press `[` key to start/stop function. Can be edited in `keymap`.

For other settings, see [Auto Combat Assist introduction](./combat_assi.md).

> 单拉出来的一个核心功能(

### 2. [自动秘境](./domain_assi.md)


- 目前最好用的功能~!

1. GUI 设置页面中设置挑战秘境的次数等.
2. Configure the team and enter the domain.
3. 进入秘境后(也可以在大世界,但要正确设置秘境名和关卡名),在GUI TaskList中选中DomainTask，点击启动任务
4. 等待导入完成后切换到原神
5. 双手离开键盘

Be careful to read the notes in [domain_assi.md](./domain_assi.md).

For other settings, sett [Auto Domain Assist introduction](./domain_assi.md).

> 冰本的地板会把人冻死，记得多带点奶...

### 3. [自动每日委托](./commission_assi.md)


Automatically search and execute daily commissions located in **Mondstadt**. Currently only some commissions that require only combat can be executed.

> For now, it can only complete this request: ASmallStepForHilichurls,Emergency,IcyIssues,ForTheHarbingers,BigIceColdCrisis,SpreadingEvil,PudgyPyrotechnicians,IncreasingDanger.

For more detiles, see [Auto Daily Commission Assist introduction](./commission_assi.md).

### 4. [领取日常奖励](./claim_reward.md)


在Task list中选择领取日常奖励，启动任务。

> 最稳定的功能(因为简单..)

### 5. [自动地脉衍出](./ley_line_ourcrop.md)

自动刷位于**蒙德**的`地脉衍出·启示之花`和`地脉衍出·藏金之花`。

在设置页面中设置次数和类型。

Select the Ley Line Outcrop in the Task list and start the task.

### 6. [Mission(素材收集)](./mission.md)

在自定义任务中启用你要运行的自定义任务，按照提示填写参数，保存后在主界面选择自定义任务，启动GIA。

关于创建自定义任务，参见[创建自定义任务](./dev/mission.md)

### 7. launch genshin


帮你点击`点击进入`按钮，不能帮你启动原神。

### -1. [自动采集辅助](./collector_assi.md)

> 非常垃圾，但是通用


- 在自定义任务中选择通用自动采集，启动自定义任务
- 注意阅读[collector_assi.md](./collector_assi.md)中的注意事项.

For other settings, see[Auto Collector Assist introduction](./collector_assi.md).

## 参与开发

如果你想参与GIA的开发，可以从[GIA Dev Document](./dev/readme.md)开始。

## How to use


### Quick installation


See [GIA Launcher Auto Installer Tutorial](install.md).

### Run from source code


See [Source code running tutorial](git_install.md)

## Pre-use settings


### Progress in Genshin


- 需要解锁`层岩巨渊 地下矿区`的地图。
- 需要解锁璃月与蒙德的所有传送锚点，副本式秘境

### Genshin window settings


- Need to run GIA after the Genshin Impact starts.
- The Genshin needs to run in 1080p window (full screen is also possible), set anti-aliasing to SMAA, effects to meduim or above.
- The focus of windows shoule be on Genshin window. If the focus window is switched to another window, the program will pause all the operation of keyboard and mouse and wait.

### Config configuration


Before use, these configuration elements shoule be noted:

|Path|Configuration|Content|
|----|----|----|
|config/settings/config.json| `BorderlessWindow` | When using boradless window or full screen, set to true.|

Can be modified in the GUI or directly from the file.

For other configurations, see the notes of settings within the GUI.

### [GUI使用](./gui.md)


## Bug report


如果在使用中遇到问题，可以提交issue反馈。

Please make sure you have read the document and [FAQ](FAQ.md) before feedback bugs.

反馈错误时，请一并提交 `Logs` 文件夹中的日志文件。

> Troubleshooting any problems without the error log is like driving with your eyes closed.

> -- Apache Official Document: Getting Start

<!-- ## 错误码

如果日志输出了`ERR_CODE`或`WARN_CODE`，可以在[ERROR_CODE](error_code.md)中查看对应的信息： -->

## Known issues


[Known issues](known_issues.md)

## Performance requirements


- This program requires at least `2.5G` RAM and `4G` storage space (full installation).

## Internationalization


GIA supports Simplified Chinese(zh_CN,zh_MO,zh_HK,zh_TW,zh_SG) and English(other) now.

English language support may not be comprehensive. If you are experiencing problems, please submit an issue for feedback.

GIA is using `py-gettext-markdown` to support document internationalization. The English version of docs may be delayed.

## Acknowledgements


### Special Thanks


- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript)

#### Open Source Library


### Genshin Related


- [GenshinImpact AutoTrack DLL](https://github.com/GengGode/cvAutoTrack)

- [kongying-tavern/yuan-shen-map](https://github.com/kongying-tavern/yuan-shen-map)

- [xicri/genshin-dictionary](https://github.com/xicri/genshin-dictionary)

#### Open source library


- [opencv](https://github.com/opencv/opencv)
- [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)
- [yolox](https://github.com/Megvii-BaseDetection/YOLOX)
- [pyinstaller](https://github.com/pyinstaller/pyinstaller)

#### Others


- [GIS](https://github.com/phonowell/genshin-impact-script)

### Other Contributors


- Dataset labeling: [nɡ.](https://space.bilibili.com/396023811)

