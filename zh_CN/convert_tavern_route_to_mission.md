# 转换空荧酒馆路线为自定义任务

## 简介

将空荧酒馆的路线转换为自定义任务。

## 方法

> `方形控制点`=`路径点`=`BP`

### 空荧酒馆

1. 在空荧酒馆中创建新画布，打开编辑模式
2. 参照空荧酒馆中的说明操作，路线应从传送锚点或七天神像开始。
3. 只有方形控制点会被使用，圆形控制点将被抛弃。
4. 编辑完成后导出画布为json文件

### GIA

1. 打开GUI，点击`转换空荧酒馆路线到自定义任务`按钮
2. 选择你的画布文件，点击`分析路线`按钮，将显示沿途可能采集物（注意：不代表可以采集到这些采集物，仅用于区分可能的路线名称混淆和便于下面填写采集物名！）
3. 填写采集物名，任务名，文件名，作者等信息，按照提示勾选下面的额外设置。
4. 点击`从xxxx生成自定义任务`按钮，自定义任务文件将保存在`./local_edit_mission`
5. 点击`自定义任务设置`按钮，启用刚刚生成的自定义任务
6. 在主菜单启动自定义任务，测试一下

### 额外设置

- 采集物是否在悬崖上

- 是否禁用自动吸附 [自动吸附功能介绍](../zh_CN/dev/TianLiCopilot.md)

- 是否在路径点处启动主动采集 [主动采集介绍](../zh_CN/dev/TianLiCopilot.md)

- 是否需要纳西妲：启用后，将添加需要纳西妲的提示。即使不启用该功能，仍然会在队伍中有纳西妲的情况下使用纳西妲采集。

### 注意事项

1. 一个画布应该只有一条路线，否则可能解析混乱（所有的路线名称都是`新的路线`）
2. 只有方形控制点会被使用，圆形控制点将被抛弃。
3. 如果任务需要纳西妲，请勾选对应单选框

### 技巧

- 使用纳西妲时，不一定需要将方形控制点标记在采集物上，可标记在采集物附近，并启用`在路径点处启动主动采集`。
- 采集物在悬崖上时，可将方形控制点标记在山脚下，并启用`在路径点处启动主动采集`。

### 分享自定义任务

本地自定义任务位置：`./local_edit_missions`

- https://github.com/GenshinImpactAssistant/GIA-Missions 查看具体操作方法
- 如果不会PR，开个issue，把自定义任务扔上去

## TODO（需要帮助）

- 生成圣遗物类型自定义任务（添加一个选项，设置meta的tags类型为采集/圣遗物）
- 保存GUI输入结果
- 优化吸附点选择
