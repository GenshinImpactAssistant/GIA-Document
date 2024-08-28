# 路径记录器

路径记录器是一个记录行走路线的工具。

## How to use

- 在半自动功能中选择路径记录
- 按下"\["键启动程序
- 启动完成后，按下k键开始记录，按照游戏内提示操作。
- 记录完成后，按下k键停止记录，记录文件会保存到dev_assets/tlpp中。
- 在记录过程中，可以按下p键暂停/继续记录。

## 文件生成

运行结束后，将会在dev_assets/tlpp中以时间命名，生成json和py两个文件。

其中，py文件可以直接运行。运行文件后，程序将按照刚刚记录的路径走一遍。 可以使用pycharm运行py文件, 或者使用命令行运行。

json文件可用于在GIA主界面中，用于“从路径生成自定义任务”功能。

有关自定义任务，参见[Mission](mission.md)