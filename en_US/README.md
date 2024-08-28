# Genshin Impact Assistant

<div align="center">

A multi-functional auto-assist based on image recognition and keystroke simulation, including auto combat, auto domain and auto claim materials in Teyvat world.

The aim of GIA is: let the program play Genshin, and you just need to selected characters and raise them.

[![GitHub Star](https://img.shields.io/github/stars/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/stargazers)
[![Release Download](https://img.shields.io/github/downloads/infstellar/genshin_impact_assistant/total?style=flat-square)](./install.md)
[![Release Version](https://img.shields.io/github/v/release/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/releases/latest)
[![Python Version](https://img.shields.io/badge/python-v3.7.6-blue?style=flat-square)](https://www.python.org/downloads/release/python-376/)
[![GitHub Repo Languages](https://img.shields.io/github/languages/top/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/search?l=Python)
[![GitHub Repo size](https://img.shields.io/github/repo-size/infstellar/genshin_impact_assistant?style=flat-square&color=3cb371)](https://github.com/infstellar/genshin_impact_assistant/)
[![contributors](https://img.shields.io/github/contributors/infstellar/genshin_impact_assistant?style=flat-square)](https://github.com/infstellar/genshin_impact_assistant/graphs/contributors)
</br>
[![QQ Guild](https://img.shields.io/badge/QQ%20Guild-78l224i0o1-blue.svg?style=flat-square&color=12b7f5&logo=tencentqq)](https://pd.qq.com/s/a376nvjoq)
[![QQ Group](https://img.shields.io/badge/QQ%20Group-883225524-blue.svg?style=flat-square&color=12b7f5&logo=tencentqq)](https://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=3CaUl6AyqWoM8nBm8nzcF5QrJIAPg-hL)
[![Bilibili](https://img.shields.io/badge/bilibili-infstellar-blue.svg?style=flat-square&logo=bilibili)](https://space.bilibili.com/313212782)<!-- ignore gettext -->

</div>

## Introduction

An Genshin automatic operation assistance based on image recognization and similated keyboard operation. Does not involve not-allowed operation.

To those who have not used github: the blue text in the docs is a hyperlink that can be clicked.

> This is the document repository, please click star to go to the main repository <del>(you can also star the document repo if you want)</del>

## Quick Start

If you don't want to read anything and just want to get started, follow [this method](jijiking.md)

- 注意：windows11系统用户请查看FAQ(常见问题)

## Demo Video

<https://www.bilibili.com/video/BV1RV4y157m6>(hung up)

Addendum <https://www.youtube.com/watch?v=ZieBDx6Go4A> v0.2.0 demo video, may be partially out of date.

## Function Details

Most of the functions only need to set the parameters, put the game in the big world, select the function and start it.

If you have doubts about a function or want to know more information, please refer to [Detailed Function Introduction](functions_detail.md).

- 注意：windows11系统用户请查看FAQ(常见问题)

## Frequently ask question

If you enconter any problem when using, you can take a look at FAQ frist.

## Participate in Development

非常欢迎提交PR。如果你想参与GIA的开发，可以从[GIA Dev Document](dev/README.md)开始。

## Installation

### Quick installation

参见[PGPL自动安装器使用方法](install.md)。

### Run from source code

参见[源代码安装方法](git_install.md)。

## Pre-use settings

### Progress in Genshin

- You need to unlock region map of `The Chasm: Underground Mines` first.
- You need to unlock all the teleportation points and dungeons of Liyue and Mondstadt first.

### Genshin window settings

- Need to run GIA after the Genshin Impact starts.
- The Genshin needs to run in 1080p window (full screen is also possible), set anti-aliasing to SMAA, effects to meduim or above.
- The focus of windows shoule be on Genshin window. If the focus window is switched to another window, the program will pause all the operation of keyboard and mouse and wait.

### Config configuration

Before use, these configuration elements shoule be noted:

| 位置                        | 配置项             | 内容                                                     |
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

Please see [Known issues](known_issues.md).

## Performance requirements

- This program requires at least `2.5G` RAM and `4G` storage space (full installation).

## Internationalization

GIA supports Simplified Chinese(zh_CN,zh_MO,zh_HK,zh_TW,zh_SG) and English(other) now.

English language support may not be comprehensive. If you are experiencing problems, please submit an issue for feedback.

GIA is using `py-gettext-markdown` to support document internationalization. The English version of docs may be delayed.

## Acknowledgements

Thanks to all the friends who participated in the development/testing (\*´▽｀)ノノ

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

qq群：[883225524](https://qm.qq.com/cgi-bin/qm/qr?_wv=1027&k=3CaUl6AyqWoM8nBm8nzcF5QrJIAPg-hL)

qq频道(测试)：[78l224i0o1](https://pd.qq.com/s/a376nvjoq)

Developers' Communication Group: [680029885](https://jq.qq.com/?_wv=1027&k=CGuTvCXU)

(Make sure you already know how to use git and github)
