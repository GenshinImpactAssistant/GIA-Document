# 视频转路径（video to path, or V2P）

根据视频生成路径。

位置： `source/dev_tool/video2path.py`

## 介绍

通过视频生成TLPP(TianLiPositioningPath)文件。原理和[路径记录器](path_recorder.md)基本一致,但用法不同。

运行source/dev_tool/video2path.py文件以开始分析视频。

有关更多TLPP的信息，请参阅[TLPP介绍](TianLiPositioningPath.md)。

演示视频:https://www.bilibili.com/video/BV1Lm4y1i7kj

参考视频:https://www.bilibili.com/video/BV1Lu411W71q

## 注意

- 一个连续的路径的开头应该从传送锚点开始。
- 必须是完整流畅的原神游戏录屏。
- 记录路径时，播放速度（fps）应当与真实移动速度接近。

## TLPP文件格式

运行结束后，V2P会生成xxx+timestamp+xxx.pydict文件。将该文件中的内容复制粘贴到你的自定义任务的代码中对应的位置即可。

## GUI版本

使用方法：

1. 打开DEBUG模式，重启GIA
2. 在页面中选择视频转路径
3. 按照教程操作。

## 按键

- 空格：暂停/开始播放
- a：分析传送锚点坐标
- .：加速fps
- ,：降低fps
- `]` ：开始/停止记录路径
