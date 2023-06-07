# Installation method

GIA provides an automatic installer/updater.

# GIA Auto Install Launcher

## Download

[GIA Launcher v0.6](https://github.com/infstellar/genshin_impact_assistant/releases/download/v0.6.0-beta.542/GIA_Launcher_v0.6.0.7z)注意：如果你之前下载了v0.3版本的启动器，需要全部删除(toolkit文件夹可不删除，跳过重复安装依赖)所有文件后再启动新的启动器。

## How to use

双击 `GIA Launcher.exe` 运行。

## Configuration file

对中国用户来说，可以使用 `installer_config_cn.json` 配置文件，已经根据中国特色网络环境进行了单独配置。

使用方法：删除 `installer_config.json` ，保留 `installer_config_cn.json` 即自动启用 `installer_config_cn.json` 。

具体配置(可选)：

| name                | content                                                                                                          |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| RequirementsFile    | requirements.txt file location                                                                                   |
| InstallDependencies | Whether to install dependencies, default is true                                                                 |
| PypiMirror          | Pypi mirror site.                                                                                                |
| Repository          | The address of the repository. Default to `https://github.com/GenshinImpactAssistant/GIA_Launcher_Download_Lib`. |
| GitProxy            | Switch Git SSL authentication. Defaults to false.                                                                |
| KeepLocalChanges    | Keeps local changes to files. Defaults to false                                                                  |
| AutoUpdate          | Update automatically. Defaults to true                                                                           |
| Branch              | The branch where the code will be downloaded. The following branches are available:                              |
