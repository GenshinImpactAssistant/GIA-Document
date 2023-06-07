# 视频转路径(video to path, or V2P)

根据视频生成路径。

位置： `source/dev_tool/video2path.py`

## Introduction

通过视频生成TLPP(TianLiPositioningPath)文件。原理和[路径记录器](path_recorder.md)基本一致,但用法不同。

Run the source/dev_tool/video2path.py file to start analyzing the video.

For more information about TLPP, please refer to [TLPP Introduction](TianLiPositioningPath.md)

Demo video：https://www.bilibili.com/video/BV1ks4y1Q79y

Reference video：<https://www.bilibili.com/video/BV1Lu411W71q>

## Parameters

Modify the following parameters directly in `video2path.py`:

```python
VIDEO_PATH = r"" # 填写你的视频路径
FRAME_TO_START = 0 # 填写视频播放开始帧，控制台会输出 frame:xxx来提示当前帧
PATH_HEAD_NAME = "GlazeLily" # 填写TLPP文件名开头。保存时会以该字符串作为文件名的开头。
COLL_NAME = "琉璃百合" # 填写采集物名称。务必填写正确的名称，否则生成的TLPP文件中的adsorptive_position可能为空列表。
IS_PICKUP_MODE = True # 是否为采集路径模式
```

如果 `IS_PICKUP_MODE=True` ，务必填写 `COLL_NAME` 。

## 按键

- Space: pause/start playback
- a: Analyzing Teleport Anchor Coordinates
  -. : speed up fps
- ,: reduce fps
- `]` : start/stop logging path

## How to use

- Fill in the parameters and run the program
- Before starting to move, press the key `a`, V2P will start to analyze the possible teleportation anchors of the current location.
- Enter the corresponding index in the console and press Enter to view the terrain near the teleportation anchor point (displayed by cv2).
- 按下 `]` 按键以启动记录。注意看控制台的提示。
- 一条采集路线将要结束时，按下 `]` 以结束记录。TLPP文件会保存在 `./dev/tlpp` 目录下。注意看控制台的提示。 `./dev/tlpp/QXV220230513083258i0.pydict` 是一个示例文件。

## Attantion

- The beginning of a continuous path should start from the teleport anchor
- It must be a complete and smooth screen recording of Genshin Impact Games
- When recording the path, the playback speed (fps) should be close to the real moving speed.

## TLPP文件格式

运行结束后，V2P会生成xxx+timestamp+xxx.pydict文件。将该文件中的内容复制粘贴到你的自定义任务的代码中对应的位置即可。
