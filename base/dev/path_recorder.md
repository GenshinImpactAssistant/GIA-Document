# 路径记录器

位置：flow/path_recorder_flow.py

**该文件用于游戏内路径记录。目前推荐使用GUI版的VideoToPath达到相似功能。**

**这是路径记录的底层实现，推荐使用以下两个包装后的功能记录路径：**

- [TLPP 游戏内路径记录](../record_path.md)(易于上手)
- [TLPP 视频转路径](video2path.md)

## 使用

### 加载

1. 运行path_recorder_flow.py。
2. 等待加载，会出现 `input your path name` 提示，输入你的path名。
3. 等待提示 `Load over.` `ready to start.` 即准备完成。

### 运行

1. 按下 `\` 键，提示 `ready to start recording` 。如果没有，就再按一次。
2. 一通操作后，提 `start recording` ，就可以开始移动了。
3. 移动时，所有的坐标会被记录。同时，角色的动作状态（行走，爬山等）也会被记录。
4. 角色移动方向改变超过5°时，会记录一次break position。break position之间的距离最小为5.2。
5. 走完之后，再次按下 `\` 键。提示 `ready to stop recording` 。
6. 在1秒内应该会提示 `recording save as {jsonname}` 。如果没有，就再按一次 `\` 。
7. json文件将保存为 `name+timestamp.pydict` 。如果想继续记录，就重复这些步骤。
