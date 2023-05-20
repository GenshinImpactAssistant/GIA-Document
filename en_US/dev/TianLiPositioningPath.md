# TianLiPositioningPath TLPP


> 编写中...

TLPP是保存TianLi格式坐标的文件。

## TLPP文件结构


TLPP由path_recorder_flow.py文件生成。文件结构如下:
```python
collection_path_dict = {
            "name":"",
            "time":"",
            "start_position":[],
            "break_position":[],
            "end_position":[],
            "position_list":[],
            "additional_info":{
                "pickup_points":[]
            },
            "adsorptive_position":[]
        }
```

|key|introduction|
|----|----|
|name|TLPP文件名称|
|time|TLPP文件创建时间|
|start_position|TLPP开始坐标|
|end_position|TLPP结束坐标|
|break_position|转向点坐标，用于寻路|
|position_list|路径中坐标，用于记录角色动作|
|additional_info|额外信息|
|pickup_points|采集点的BP的index|
|adsorptive_position|吸附坐标，TLC会尝试接近这个坐标|

## 屏蔽坐标
如果有某个坐标打的不好，你想要手动修改它时：
- 若 `additional_info` `pickup_points`列表为空，直接删除对应index的BP
- 否则，将对应index的BP改为与它的上一个BP或下一个BP相同。这是为了避免BP顺序错误。


