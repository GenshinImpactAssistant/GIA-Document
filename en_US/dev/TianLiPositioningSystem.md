# TLPS & TLN 


# TianLiPositioningSystem


## Introduction

TLPS是基于OpenCV的小地图定位算法，小地图视角识别算法，小地图方向识别算法，大地图定位算法和相关的集成功能。

你可以在source/map中找到相关代码。

# TianLiNavigator


## Introduction

TLN是基于A-star寻路的导航算法，工作原理如下：1. 人工标记适合行走的点位路线2. TeyvatMove中根据开始点与结束点搜索适宜节点3. 优先按照路线行走，路线结束后朝目标直线行走。

## TianLiNavigatorDev TLNDev


TLND是用于人工编辑路线的工具，位于`source/dev_tool/tianli_navigator.py`

### TLNDev基本介绍


首先，运行tianli_navigator.py。
TLND会弹出一个显示了GIMAP图片的窗口，同时命令行会等待输入。

每个点与每个点之间有箭头连接，代表它们之间的link关系。

每个点旁边有它的编号。

### TLNDev名词解释
- 全连接(full link, or fl)：意味着双向连接，比如节点1与节点2全连接意味着1<->2双向连通。

### TLNDev命令


在命令行中输入命令。

使用`;`分割数个命令。不能在`;`附近包含空格。

- undo

撤销上一次指令。只能撤销一次(懒)

- del `id`
删除指定id的节点和它的所有相关连接。

- del `id1`~`id2`
删除指定id1到id2的所有连续id。

- link `id1` `id2`
连接id1与id2。

- add `x`,`y` [id=`id`] [fl=`xxx`]
添加坐标x,y。如果不指定id，则自动使用下一个id。

可以指定要与之全连接(full link)的节点id。如果为空，则自动设为上一个id。

- add a
当你鼠标左键点击了一下图片时，会记录点击的坐标，输入add a就会自动添加这个坐标，不需要手动输入坐标。id与fl指令均可用。

连续添加坐标时，通常使用`add a fl=`命令。它意味着添加上次鼠标点击的坐标，并自动与上一个id全连接。

- save
保存。


