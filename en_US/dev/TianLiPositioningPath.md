# TianLiPositioningPath TLPP

> Being Prepared……

TLPP is a file that saves coordinates in TianLi format.

## TLPP file structure

TLPP is generated by path_recorder_flow.py file. The file structure is as follows:

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

| key                 | introduction                                                      |
| ------------------- | ----------------------------------------------------------------- |
| name                | TLPP file name                                                    |
| time                | TLPP file create time                                             |
| start_position      | TLPP start coordinates                                            |
| end_position        | TLPP end coordinates                                              |
| break_position      | Turning point coordinates, used for pathfinding                   |
| position_list       | Coordinates in the path, used to record character actions         |
| additional_info     | additional information                                            |
| pickup_points       | BP index of collection points                                     |
| adsorptive_position | adsorption coordinates, TLC will try to approach this coordinates |

## 屏蔽坐标

如果有某个坐标打的不好，你想要手动修改它时：

- If the `additional_info` `pickup_points` list is empty, directly delete the BP corresponding to the index.
- Otherwise, change the BP corresponding to the index to be the same as its previous or next BP.
