# Genshin Impact Assistant

<div align="center">

基于图像识别和模拟按键的多功能原神自动辅助操作，包括自动战斗，自动刷秘境，自动刷大世界材料等。

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

## 介绍


基于图像识别的原神自动操作辅助.使用图片识别与模拟键盘操作,不涉及违规操作.

To没用过github的小伙伴: 描述文档中的蓝色文字是链接,可以打开的.

> 这里是文档仓库，点star请到主仓库 ~~(如果你需要star文档仓库也可以)~~

## 我是急急国王


如果你啥都不想看就想开始用，按照[这个方法](zh_CN/jijiking.md)操作：

## 演示视频


<https://www.bilibili.com/video/BV1ps4y1T71A> v0.8.3

<https://www.youtube.com/watch?v=ZieBDx6Go4A> v0.2.0的演示视频，可能过期

## [常见问题 FAQ](zh_CN/FAQ.md)

如果在使用时遇到问题，先看看[FAQ](zh_CN/FAQ.md)

## [功能介绍](zh_CN/functions_detail.md)


绝大部分功能只需要设置好参数后，将游戏置于大世界，选择功能并启动。

如果你对某个功能存在疑惑或想了解更多信息，请参阅[详细功能介绍](zh_CN/functions_detail.md)

## 参与开发

非常欢迎提交PR。如果你想参与GIA的开发，可以从[GIA Dev Document](zh_CN/dev/readme.md)开始。

## Internationalization


GIA supports Simplified Chinese(zh_CN,zh_MO,zh_HK,zh_TW,zh_SG) and English(other) now.

English language support may not be comprehensive. If you are experiencing problems, please submit an issue for feedback.

GIA is using `py-gettext-markdown` to support document internationalization. The English version of docs may be delayed.

## 使用方法


### 快速安装


请参见[GIA Launcher自动安装器使用方法](zh_CN/install.md).

### 从源代码构建


请参见[源代码安装方法](zh_CN/git_install.md)

## 使用前设置


### 原神游戏进度


- 需要解锁`层岩巨渊 地下矿区`的地图。
- 需要解锁璃月与蒙德的所有传送锚点，副本式秘境

### 原神窗口设置


- 需要在原神启动后再运行程序.
- 原神需要以1080p窗口化运行(全屏也可以),设置抗锯齿为SMAA,中或以上特效.
- 窗口焦点应在原神窗口上。如果切换焦点窗口，程序会暂停所有键鼠操作并等待。

### config配置


在使用前，需要注意这些配置内容：

|位置|配置项|内容|
|----|----|----|
|设置-通用设置| `BorderlessWindow` | 如果是无边框窗口或全屏，设置为true。|

可以在GUI或直接从文件中修改。

更多其他配置项，参见GUI内的设置介绍：[GUI使用](zh_CN/gui.md)


## 错误报告


如果在使用中遇到问题，可以提交issue反馈。

反馈错误前，请务必确认您已经阅读文档和[FAQ](zh_CN/FAQ.md)中的已知问题与解决方案。

反馈错误时，请一并提交 `Logs` 文件夹中的日志文件。

> Troubleshooting any problems without the error log is like driving with your eyes closed. -- Apache Official Document: Getting Start

<!-- ## 错误码

如果日志输出了`ERR_CODE`或`WARN_CODE`，可以在[ERROR_CODE](zh_CN/error_code.md)中查看对应的信息： -->

## [已知问题 Known Issues](zh_CN/known_issues.md)


[Known issues](zh_CN/known_issues.md)

## 性能需求


- 此程序至少需要`2.5G内存`与`4G存储空间`(完整安装).

## 鸣谢


感谢所有参与到开发/测试中的朋友们 (\*´▽｀)ノノ

[![Contributors](https://contributors-img.web.app/image?repo=infstellar/genshin_impact_assistant)](https://github.com/infstellar/genshin_impact_assistant/graphs/contributors)

### 特别感谢


- [Alas](https://github.com/LmeSzinc/AzurLaneAutoScript)

### 开源库


#### 原神相关


- [空荧酒馆原神地图 kongying-tavern/yuan-shen-map](https://github.com/kongying-tavern/yuan-shen-map)
- [原神-天理坐标系](https://github.com/GengGode/cvAutoTrack)
- [原神英語・中国語辞典 xicri/genshin-dictionary](https://github.com/xicri/genshin-dictionary)
- [GIS 参考了自动战斗脚本的格式](https://github.com/phonowell/genshin-impact-script)

#### 开源库调用


- [opencv](https://github.com/opencv/opencv)
- [paddleocr](https://github.com/PaddlePaddle/PaddleOCR)
- [yolox](https://github.com/Megvii-BaseDetection/YOLOX)

### 其他贡献/参与者


- 数据集标注: [nɡ.](https://space.bilibili.com/396023811)

## 广告

qq群:[901372518](https://jq.qq.com/?_wv=1027&k=YLTrqlzX)

开发者交流群:[680029885](https://jq.qq.com/?_wv=1027&k=CGuTvCXU)
(请确保你已经会使用git以及github)

