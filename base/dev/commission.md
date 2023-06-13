# 每日委托任务

编写执行每日委托的任务脚本。

## 简介

每日委托（Commission）用于执行每日委托。根据委托名与坐标唯一确定单个委托。

因为每日委托的稀有性，适配多语言存在困难，因此所有每日委托默认使用**中文**编写和运行。（文件名还是英文，所以可能需要切换一下原神语言查看委托的英文名。）  
你可以在初始化类时使用support_lang来设置支持的语言。

Commission的编写方法与Mission基本一致，但文件命名有所不同。因此，请先看看[自定义任务](mission.md)。

你可以在[source/commission/commissions](https://github.com/infstellar/genshin_impact_assistant/tree/main/source/commission/commissions)找到一些范例。

参考视频：https://www.bilibili.com/video/BV1Lu411W71q

## 命名格式

文件名命名： `commission_name_commission_position`\
示例： BasicKnowledgeOfTheKnights_P2682N5673.py

commission坐标命名格式：(P/N)xxxC(P/N)xxx\
P代表+，N代表-。\
示例： -1000,1000 => N1000P1000

类名必须与文件名相同。

~~如果你没有看懂，那就直接PR~~

## 函数清单

函数清单和简介位于[source/commission/commission.py](https://github.com/infstellar/genshin_impact_assistant/tree/main/source/commission/commission.py)\
从该类继承。

commission专有函数清单：

| 函数                | 用途                               |
| ----------------- | -------------------------------- |
| talk_skip         | 跳过对话，直到回到大世界                     |
| talk_switch       | 选择选项                             |
| talk_until_switch | 对话直到出现选项                         |
| talk_wait         | 等待x秒                             |
| talk_with_npc     | 与指定名称的NPC对话。会按wasd改变方向来寻找附近的NPC。 |
| exit_talk         | 退出对话，直到返回主界面。                    |

## 获得当前坐标

如果你是VSCode用户，在 `运行和调试` 中选择 `Python: Get Position` 运行，切换到原神即可。\
否则，请运行 `source\commission\dev_tools\get_position.py` 文件。

## 调试Commission

```python
if __name__ == '__main__':
    execc = BasicKnowledgeOfTheKnights_P2682N5673()
    execc.start()
```

## 添加Commission到GIA

这个过程比较麻烦，因此请直接PR你的Commission。
