# TLPS & TLN

## TianLiPositioningSystem

### Introduction

TLPS is a small map positioning algorithm based on OpenCV, a small map perspective recognition algorithm, a small map direction recognition algorithm, a large map positioning algorithm and related integration functions.

You can find the relevant code in source/map.

## TianLiNavigator

### Introduction

TLN is a navigation algorithm based on A-star pathfinding, the working principle is as follows:

1. Manually mark the point routes suitable for walking
2. In TeyvatMove, search for suitable nodes according to the start point and end point
3. Prioritize walking according to the route, and walk straight to the goal after the route ends.

### TianLiNavigatorDev

TLNDev是用于人工编辑路线的工具，位于 `source/dev_tool/tianli_navigator.py`

#### TLNDev基本介绍

首先，运行tianli_navigator.py。TLND会弹出一个显示了GIMAP图片的窗口，同时命令行会等待输入。

There is an arrow connection between each point and each point, representing the link relationship between them.

Each point has its number next to it.

### TLNDev名词解释

- Full link (full link or fl): means two-way connection, such as full connection between node 1 and node 2 means 1\<->2 bidirectional connectivity.

#### TLNDev命令

在命令行中输入命令。

Use `;` to split several commands.

- undo

  Cancel the last command.

- del `id`
  Delete the node with the specified id and all its related connections.

- del `id1`~`id2`
  Delete all consecutive ids from the specified id1 to id2.

- link `id1` `id2`
  Connect id1 and id2.

- add `x`,`y` \[id=`id`\] \[fl=`xxx`\]
  Add coordinates x,y.

  You can specify the node id to be fully connected with (full link).

- add a
  When you click the picture with the left mouse button, the coordinates of the click will be recorded. Inputting add a will automatically add the coordinates, no need to manually enter the coordinates.

When adding coordinates continuously, the `add a fl=` command is usually used.

- save
  Save.
