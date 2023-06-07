# Installation method

GIA provides an automatic installer/updater.

# GIA Auto Install Launcher

## Download

[GIA Launcher v0.6](https://github.com/infstellar/genshin_impact_assistant/releases/download/v0.6.0-beta.542/GIA_Launcher_v0.6.0.7z)
Note: If you have previously downloaded the v0.3 launcher, you will need to delete all files (but not the toolkit folder, to skip duplicate installation dependencies) before launching the new launcher.

## How to use

Double click on `GIA Launcher.exe` to run it.

## Configuration file

对中国用户来说，可以使用 `installer_config_cn.json` 配置文件，已经根据中国特色网络环境进行了单独配置。

使用方法：删除 `installer_config.json` ，保留 `installer_config_cn.json` 即自动启用 `installer_config_cn.json` 。

Specific configuration.

| 项目                  | 内容                                                                                                               |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| RequirementsFile    | requirements.txt文件位置                                                                                             |
| InstallDependencies | 是否安装依赖文件，默认为true                                                                                                 |
| PypiMirror          | Pypi mirror site.                                                                                                |
| Repository          | The address of the repository. Default to `https://github.com/GenshinImpactAssistant/GIA_Launcher_Download_Lib`. |
| GitProxy            | 开关Git SSL验证。默认为false                                                                                             |
| KeepLocalChanges    | 保持本地文件更改。默认为false                                                                                                |
| AutoUpdate          | 自动更新。默认为true                                                                                                     |
| Branch              | The branch where the code will be downloaded. The following branches are available:                              |
