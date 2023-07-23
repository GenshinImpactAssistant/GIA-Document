# 视频转路径（video to path, or V2P）

根据视频生成路径。

位置： `source/dev_tool/video2path.py`

## Introduction

通过视频生成TLPP(TianLiPositioningPath)文件。原理和[路径记录器](path_recorder.md)基本一致,但用法不同。

Run the source/dev_tool/video2path.py file to start analyzing the video.

For more information about TLPP, please refer to [TLPP Introduction](TianLiPositioningPath.md).

演示视频:https://www.bilibili.com/video/BV1Lm4y1i7kj

Reference video：<https://www.bilibili.com/video/BV1Lu411W71q>

## Attantion

- The beginning of a continuous path should start from the teleport anchor.
- It must be a complete and smooth screen recording of Genshin Impact Games.
- When recording the path, the playback speed (fps) should be close to the real moving speed.

## TLPP文件格式

运行结束后，V2P会生成xxx+timestamp+xxx.pydict文件。将该文件中的内容复制粘贴到你的自定义任务的代码中对应的位置即可。

## GUI版本

使用方法：

1. 打开DEBUG模式，重启GIA
2. 在页面中选择视频转路径
3. 按照教程操作。

## 按键

- Space: pause/start playback
- a: Analyzing Teleport Anchor Coordinates
  -. : speed up fps
- ,: reduce fps
- `]` : start/stop logging path
