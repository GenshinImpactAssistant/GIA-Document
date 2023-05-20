# 视频转路径(video to path, or V2P)


根据视频生成路径。

位置：`source/dev_tool/video2path.py`

## 介绍

通过视频生成TLPP(TianLiPositioningPath)文件。原理和[路径记录器](./path_recorder.md)基本一致,但用法不同。

运行source/dev_tool/video2path.py文件以开始分析视频。

有关更多TLPP的信息，请参阅[TLPP介绍](./tianli_positioning_path.md)

演示视频:https://www.bilibili.com/video/BV1ks4y1Q79y

## 参数
在`video2path.py`中直接修改以下参数：
```python
VIDEO_PATH = r"" # 填写你的视频路径
FRAME_TO_START = 0 # 填写视频播放开始帧，控制台会输出 frame:xxx来提示当前帧
PATH_HEAD_NAME = "GlazeLily" # 填写TLPP文件名开头。保存时会以该字符串作为文件名的开头。
COLL_NAME = "琉璃百合" # 填写采集物名称。务必填写正确的名称，否则生成的TLPP文件中的adsorptive_position可能为空列表。
IS_PICKUP_MODE = True # 是否为采集路径模式
```

如果`IS_PICKUP_MODE`=True，务必填写`COLL_NAME`。

## 按键
- 空格：暂停/开始播放
- a：分析传送锚点坐标
- .：加速fps
- ,：降低fps
- `]`：开始/停止记录路径

## 使用方法：
- 填写参数，运行程序
- 在开始移动前，按下按键`a`，V2P会开始解析当前位置可能的传送锚点。解析完成后，会在控制台弹出所有可能的传送锚点坐标和index。注意看控制台的提示。
- 在控制台输入对应的index，按下回车，可以查看该传送锚点附近的地形(使用cv2显示)。如果地形符合，在控制台直接按下空格以确认。注意看控制台的提示。
- 按下`]`按键以启动记录。注意看控制台的提示。
- 一条采集路线将要结束时，按下`]`以结束记录。TLPP文件会保存在`./dev/tlpp`目录下。注意看控制台的提示。`./dev/tlpp/QXV220230513083258i0.pydict`是一个示例文件。

## 注意
- 连续的路径的开头必须从传送锚点开始
- 必须是完整流畅的原神游戏录屏
- 记录路径时，播放速度(fps)应当与真实移动速度接近。

## TLPP文件格式

运行结束后，V2P会生成xxx+timestamp+xxx.pydict文件。将该文件中的内容复制粘贴到你的自定义任务的代码中对应的位置即可。

