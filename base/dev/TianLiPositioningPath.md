# TianLiPositioningPath TLPP

> 编写中……

TLPP是保存TianLi格式坐标的文件。

## TLPP文件结构

TLPP由path_recorder_flow.py文件生成。文件结构如下：

```python
collection_path_dict = {
            "name":"",
            "time":"",
            "start_position":[],
            "break_position":[],
            "end_position":[],
            "position_list":[],
            "additional_info":{
                "pickup_points":[],
                "adsorptive_position": [],
                "is_cliff_collection":True|False,
                "is_active_pickup_in_bp":True|False,
            },
            "adsorptive_position":[]
        }
```

由tavern2mission生成的版本：

```python
collection_path_dict = {
            "name":"",
            "time":"",
            "start_position":[],
            "break_position":[],
            "end_position":[],
            "position_list":[],
            "additional_info":{
                "pickup_points":[],
                "kyt2m_version": "1.0", 
                "pickup_points": [], 
                "adsorptive_position": [],
                "is_cliff_collection":True|False,
                "is_active_pickup_in_bp":True|False,
                "ads_offset":float=10
                "bp_ads_offset":float=30
            },
            "adsorptive_position":[]
        }
```

| key                    | introduction      |
| ---------------------- | ----------------- |
| name                   | TLPP文件名称          |
| time                   | TLPP文件创建时间        |
| start_position         | TLPP开始坐标          |
| end_position           | TLPP结束坐标          |
| break_position         | 转向点坐标，用于寻路        |
| position_list          | 路径中坐标，用于记录角色动作    |
| additional_info        | 额外信息              |
| pickup_points          | 采集点的BP的index      |
| adsorptive_position    | 吸附坐标，TLC会尝试接近这个坐标 |
| is_cliff_collection    | 采集物是否在悬崖上         |
| is_active_pickup_in_bp | 是否在BP处激活主动采集      |


