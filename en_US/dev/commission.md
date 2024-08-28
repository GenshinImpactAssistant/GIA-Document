# Automatic Daily Commission

Write a task script to execute the daily commission.

## Introduction

Daily commission (Commission) is used to execute daily commission. A single commission is uniquely determined according to the commission name and coordinates.

因为每日委托的稀有性，适配多语言存在困难，因此所有每日委托默认使用**中文**编写和运行。（文件名还是英文，所以可能需要切换一下原神语言查看委托的英文名。）

你可以在初始化类时使用support_lang来设置支持的语言。

The writing method of Commission is basically the same as that of Mission, but the file naming is different. Therefore, please take a look at [Custom Mission](mission.md).

You can find some examples at [source/commission/commissions](https://github.com/infstellar/genshin_impact_assistant/tree/main/source/commission/commissions).

Reference video：<https://www.bilibili.com/video/BV1Lu411W71q>

## 命名格式

文件名命名： `commission_name_commission_position`

示例： BasicKnowledgeOfTheKnights_P2682N5673.py

Commission coordinate naming format: (P/N)xxxC(P/N)xxx

P stands for +, N stands for -.

Example: -1000,1000 => N1000P1000

The class name must be the same as the file name.

~~If you don’t understand, then just PR~~

## 函数清单

函数清单和简介位于[source/commission/commission.py](https://github.com/infstellar/genshin_impact_assistant/tree/main/source/commission/commission.py)

Inherited from the MissionExecutor class.

List of functions:

| 函数              | 用途                                                                                                            |
| ----------------- | --------------------------------------------------------------------------------------------------------------- |
| talk_skip         | 跳过对话，直到回到大世界                                                                                        |
| talk_switch       | 选择选项                                                                                                        |
| talk_until_switch | 对话直到出现选项                                                                                                |
| talk_wait         | 等待x秒                                                                                                         |
| talk_with_npc     | Talk to the NPC with the specified name. It will change the direction according to wasd to find the nearby NPC. |
| exit_talk         | 退出对话，直到返回主界面。                                                                                      |

## 获得当前坐标

如果你是VSCode用户，在 `运行和调试` 中选择 `Python: Get Position` 运行，切换到原神即可。

否则，请运行 `source\commission\dev_tools\get_position.py` 文件。

## 调试Commission

```python
if __name__ == '__main__':
    execc = BasicKnowledgeOfTheKnights_P2682N5673()
    execc.start()
```

## 添加Commission到GIA

这个过程比较麻烦，因此请直接PR你的Commission。
