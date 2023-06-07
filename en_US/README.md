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
[![QQ群](https://img.shields.io/badge/QQ%E7%BE%A4-901372518-blue.svg?style=flat-square&color=12b7f5&logo=qq)](https://jq.qq.com/?_wv=1027&k=YLTrqlzX)
[![Bilibili](https://img.shields.io/badge/bilibili-infstellar-blue.svg?style=flat-square&logo=bilibili)](https://space.bilibili.com/313212782)<!-- ignore gettext -->

</div>

## Introduction

An Genshin automatic operation assistance based on image recognization and similated keyboard operation. Does not involve not-allowed operation.

To those who have not used github: the blue text in the docs is a hyperlink that can be clicked.

> 这里是文档仓库，点star请到主仓库 ~~(如果你需要star文档仓库也可以)~~

## Quick Start

If you don't want to read anything and just want to get started, follow [this method](jijiking.md)

## Demo Video

<https://www.bilibili.com/video/BV1RV4y157m6>(hung up)

Addendum <https://www.youtube.com/watch?v=ZieBDx6Go4A> v0.2.0 demo video, may be partially out of date.

## Frequently ask question

If you enconter any problem when using, you can take a look at FAQ frist

## Function Details

绝大部分功能只需要设置好参数后，将游戏置于大世界，选择功能并启动。

如果你对某个功能存在疑惑或想了解更多信息，请参阅[详细功能介绍](functions_detail.md)

## 参与开发

非常欢迎提交PR。如果你想参与GIA的开发，可以从[GIA Dev Document](dev/)开始。

## Internationalization

GIA supports Simplified Chinese(zh_CN,zh_MO,zh_HK,zh_TW,zh_SG) and English(other) now.

English language support may not be comprehensive. If you are experiencing problems, please submit an issue for feedback.

GIA is using `py-gettext-markdown` to support document internationalization. The English version of docs may be delayed.

## How to use

### Quick installation

See [GIA Launcher Auto Installer Tutorial](install.md).

### Run from source code

See [Source code running tutorial](git_install.md)

## Pre-use settings

### Progress in Genshin

- 需要解锁 `层岩巨渊 地下矿区` 的地图。
- 需要解锁璃月与蒙德的所有传送锚点，副本式秘境

### Genshin window settings

- Need to run GIA after the Genshin Impact starts.
- The Genshin needs to run in 1080p window (full screen is also possible), set anti-aliasing to SMAA, effects to meduim or above.
- The focus of windows shoule be on Genshin window. If the focus window is switched to another window, the program will pause all the operation of keyboard and mouse and wait.

### Config configuration

Before use, these configuration elements shoule be noted:

| name                        | configuration      | content                                                  |
| --------------------------- | ------------------ | -------------------------------------------------------- |
| config/settings/config.json | `BorderlessWindow` | When using boradless window or full screen, set to true. |

Can be modified in the GUI or directly from the file.

For other configurations, see the notes of settings within the GUI.

## Bug report

If you encounter ploblems in using, you can create an issue or give a feedback in qq group or discord.

Please make sure you have read the document and [FAQ](FAQ.md) before feedback bugs.

Please send the log file in the Logs folder when you feedback.

> Troubleshooting any problems without the error log is like driving with your eyes closed.
>
> ——Apache Official Document: Getting Start

<!-- ## ERR Code

If the log outputs `ERR_CODE` or `WARN_CODE`, you can see the corresponding information in [ERROR_CODE](error_code.md). -->

## [Known issues](known_issues.md)

[Known issues](known_issues.md)

## Performance requirements

- This program requires at least `2.5G` RAM and `4G` storage space (full installation).

## Acknowledgements

感谢所有参与到开发/测试中的朋友们 (\*´▽｀)ノノ

[![Contributors](https://contributors-img.web.app/image?repo=infstellar/genshin_impact_assistant)](https://github.com/infstellar/genshin_impact_assistant/graphs/contributors)

### Special Thanks

- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript)

### Open Source Library

#### Genshin Related

- [kongying-tavern/yuan-shen-map](https://github.com/kongying-tavern/yuan-shen-map)
- [GenshinImpact AutoTrack DLL](https://github.com/GengGode/cvAutoTrack)
- [xicri/genshin-dictionary](https://github.com/xicri/genshin-dictionary)
- [GIS](https://github.com/phonowell/genshin-impact-script)

#### Open source library

- [opencv](https://github.com/opencv/opencv)
- [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)
- [yolox](https://github.com/Megvii-BaseDetection/YOLOX)

### Other Contributors

- Dataset labeling: [nɡ.](https://space.bilibili.com/396023811)

## Ads

QQ group:[901372518](https://jq.qq.com/?_wv=1027&k=YLTrqlzX)

Developers' Communication Group: [680029885](https://jq.qq.com/?_wv=1027&k=CGuTvCXU)
(Make sure you already know how to use git and github)
