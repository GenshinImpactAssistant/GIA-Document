# TLPS & TLN

## TianLiPositioningSystem

### 介绍

TLPS是基于OpenCV的小地图定位算法，小地图视角识别算法，小地图方向识别算法，大地图定位算法和相关的集成功能。\
你可以在source/map中找到相关代码。如果你想要获得更多信息并参与开发，提交issue或在QQ群讨论。

## TianLiNavigator

### 介绍

TLN是基于A-star寻路的导航算法，工作原理如下：

1. 人工标记适合行走的点位路线。
2. TeyvatMove中根据开始点与结束点搜索适宜节点。
3. 优先按照路线行走，路线结束后朝目标直线行走。

### TianLiNavigatorDev

TLNDev是用于人工编辑路线的工具，位于 `source/dev_tool/tianli_navigator.py`

### 演示视频

https://www.bilibili.com/video/BV1zb421E7MN

#### TLNDev基本介绍

首先，运行tianli_navigator.py。
TLND会弹出一个显示了GIMAP图片的窗口，同时命令行会等待输入。\
每个点与每个点之间有箭头连接，代表它们之间的link关系。\
每个点旁边有它的uuid。

<strong>注意：从Pycharm运行这个文件会导致plt卡死，请使用vscode或者命令行运行。</strong>

#### TLNDev命令

在命令行中输入命令。\
使用 `;` 分割数个命令。不能在 `;` 附近包含空格。\
备注：

1. 全连接（full link或fl）：意味着双向连接，比如节点1与节点2全连接意味着1\<->2双向连通。
2. 输入uuid时，不需要输入完整的uuid，只需要输入任意一段，能够唯一标识即可。例：uuid:e6b00580-1f94-443a-8d22-05c7e119bc9a可以只输入443a，程序将自动查找其唯一对应的完整uuid。如果查找不到或找到多个将提示。
3. 当你鼠标左键点击了一下图片时，会记录点击的坐标，输入add a就会自动添加这个坐标，不需要手动输入坐标。id与fl指令均可用。

- undo\
  撤销上一次指令。只能撤销一次（懒）。

- del `id`\
  删除指定id的节点和它的所有相关连接。

- link `id1` `id2`\
  连接id1与id2。

- add `x`,`y` \[fl=`xxx`\] \[l=`xxx`\]\
  添加坐标x，y。如果不指定id，则自动创建下一个id。\
  参数：

  - fl: 指定要与之全连接的节点id
  - l: 从某个节点链接到该节点。

  两参数互斥。

- add a \[fl=`xxx`\]
  当你鼠标左键点击了一下图片时，会记录点击的坐标，输入add a就会自动添加这个坐标，不需要手动输入坐标。

连续添加坐标时，通常使用 `add a fl=xxx` 命令。它意味着添加上次鼠标点击的坐标。

- save
  保存。
