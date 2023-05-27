# 每日委托任务

编写执行每日委托的任务.

## Introduction

每日委托(Commission)用于执行每日委托.根据委托名与坐标唯一确定单个委托.

因为每日委托的稀有性,适配多语言十分困难,因此所有每日委托使用**全英文**编写和运行.旧版本的Commission可能支持多语言,但此后不再默认支持.

Commission的编写方法与Mission完全一致,但文件命名有所不同.

## 命名格式


文件名命名: `commission_name`_`commission_position`

示例: BasicKnowledgeOfTheKnights_P2682N5673.py

commission坐标命名格式:(P/N)xxxC(P/N)xxx

P代表+,N代表-.

示例: -1000,1000 => N1000P1000


类名必须与文件名相同.

你可以在`source/commission/commissions`找到一些范本.


