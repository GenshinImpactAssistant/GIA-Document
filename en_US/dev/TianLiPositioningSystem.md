# TLPS & TLN

## TianLiPositioningSystem

### Introduction

TLPS is a small map positioning algorithm based on OpenCV, a small map perspective recognition algorithm, a small map direction recognition algorithm, a large map positioning algorithm and related integration functions.

你可以在source/map中找到相关代码。如果你想要获得更多信息并参与开发，提交issue或在QQ群讨论。

### 演示视频

https://www.bilibili.com/video/BV1zb421E7MN

## TianLiNavigator

### Introduction

TLN is a navigation algorithm based on A-star pathfinding, the working principle is as follows:

1. Manually mark the point routes suitable for walking.
2. In TeyvatMove, search for suitable nodes according to the start point and end point.
3. Prioritize walking according to the route, and walk straight to the goal after the route ends.

### TianLiNavigatorDev

TLNDev是用于人工编辑路线的工具，位于 `source/dev_tool/tianli_navigator.py`

#### TLNDev基本介绍

首先，运行tianli_navigator.py。TLND会弹出一个显示了GIMAP图片的窗口，同时命令行会等待输入。

There is an arrow connection between each point and each point, representing the link relationship between them.

每个点旁边有它的uuid。

<strong>注意：从Pycharm运行这个文件会导致plt卡死，请使用vscode或者命令行运行。</strong>

#### TLNDev命令

在命令行中输入命令。

Use `;` to split several commands. There should not be spaces around `;`.

1. 全连接（full link或fl）：意味着双向连接，比如节点1与节点2全连接意味着1\<->2双向连通。
2. 输入uuid时，不需要输入完整的uuid，只需要输入任意一段，能够唯一标识即可。例：uuid:e6b00580-1f94-443a-8d22-05c7e119bc9a可以只输入443a，程序将自动查找其唯一对应的完整uuid。如果查找不到或找到多个将提示。
3. 当你鼠标左键点击了一下图片时，会记录点击的坐标，输入add a就会自动添加这个坐标，不需要手动输入坐标。id与fl指令均可用。

- undo

  Cancel the last command. You can only cancel once.

- del `id`

  Delete the node with the specified id and all its related connections.

- link `id1` `id2`

  Connect id1 and id2.

- add `x`,`y` \[fl=`xxx`\] \[l=`xxx`\]

  添加坐标x，y。如果不指定id，则自动创建下一个id。

  参数：

  - fl: 指定要与之全连接的节点id
  - l: 从某个节点链接到该节点。

  两参数互斥。

- add a \[fl=`xxx`\]
  当你鼠标左键点击了一下图片时，会记录点击的坐标，输入add a就会自动添加这个坐标，不需要手动输入坐标。

连续添加坐标时，通常使用 `add a fl=xxx` 命令。它意味着添加上次鼠标点击的坐标。

- save
  Save.
