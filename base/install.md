# 安装方法

GIA提供了自动安装/更新器。

# GIA 自动安装启动器

## 下载

[GIA Launcher v0.6](https://github.com/infstellar/genshin_impact_assistant/releases/download/v0.6.0-beta.542/GIA_Launcher_v0.6.0.7z)
注意：如果你之前下载了v0.3版本的启动器，需要全部删除(toolkit文件夹可不删除，跳过重复安装依赖)所有文件后再启动新的启动器。

## 使用方式

双击`GIA Launcher.exe`运行。

## 配置文件

对中国用户来说，可以使用`installer_config_cn.json`配置文件，已经根据中国特色网络环境进行了单独配置。

使用方法：删除`installer_config.json`，保留`installer_config_cn.json`即自动启用`installer_config_cn.json`。

具体配置：

| 项目                  | 内容                                    |
|---------------------|-----------------------------|
| RequirementsFile    | requirements.txt文件位置                  |
| InstallDependencies | 是否安装依赖文件，默认为true                      |
| PypiMirror          | Pypi镜像网站，国内用户需要设置为 `https://pypi.tuna.tsinghua.edu.cn/simple` 或其他国内镜像源。                  |
| Repository          | 仓库地址。默认为 `https://github.com/GenshinImpactAssistant/GIA_Launcher_Download_Lib` ，国内用户可设置为 `https://gitee.com/GenshinImpactAssistant/GIA_Launcher_Download_Lib` 加速访问速度。 |
| GitProxy            | 开关Git SSL验证。默认为false                  |
| KeepLocalChanges    | 保持本地文件更改。默认为false                     |
| AutoUpdate          | 自动更新。默认为true                          |
| Branch              | 代码下载的分支。有以下分支可供选择：                    |
