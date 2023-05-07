# FAQ

## 无法运行

Q: 程序崩溃？

- 检查文件路径是否为全英文或下划线
- 检查submodule是否clone成功
- 如果提示`no module name win32gui`, 请重启GIA Launcher。

Q: 启动GIA Launcher后跳出大量文字卡住怎么办？

- 是pip正在复制文件, 如果没有报错, 等待即可.
- 注意窗口是否出现 `选择：GIA Launcher`的<strong>选择</strong>字样。如果出现，请按下回车以继续程序。 GIA Launcher的本体是bat批处理文件，在点击命令窗口后会暂停，所以不要点击命令行界面。

## 运行时问题

Q: 显示ERROR：截图失败 怎么办？  
- 若shape=0,0,4 ,那么请确认原神窗口没有最小化。
- 若shape=xxx,xxx,4, 那么请确认原神分辨率为1080p，同时确认原神启动器窗口关闭。
- 如果系统是Windows11，请按照这个[issue](https://github.com/GengGode/cvAutoTrack/issues/9)设置

Q: 战斗时，设置了策略，但不切换到Q技能已经就绪的角色怎么办？  
- 检查特效是否为中或以上。

Q: 在大地图总是点歪怎么办？  
- 看看有没有设置readme中的`使用前config配置`。
- 目前对传送至周本式秘境，稻妻地图的支持尚不完备。将来会适配。