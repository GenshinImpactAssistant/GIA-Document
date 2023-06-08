# TianLiCopilot

TLC (TianLiCopilot) is based on TeyvatMoveFlow (TMF) Teyvat mobile control flow.

TLC uses \[TLPS\] (TianLiPositioningSystem) positioning.

## Introduction

TLC contains 2 modes: `AUTO` and `PATH`.

In AUTO mode, the program will combine [TLN](TianLiPositioningSystem) to move towards the goal.

In PATH mode, the program will use the [TLPP](TianLiPositioningPath.md) file to drive along the route.

## Working Principle

### AUTO mode

AUTO mode will go straight towards the target coordinate direction.

If TLN (TianLi Positioning Navigator) is enabled, TLN will be used for auxiliary navigation.

[TLPS&TLN](TianLiPositioningSystem.md)

### PATH mode

PATH mode will advance along the coordinates.

01. Moving towards the break position.
02. Automatically identify the current position, detect motion and process it.
03. If the current distance from the adsorption point is less than the allowable adsorption distance, start moving to the target adsorption point.
04. Auto Loot (if enabled).
05. Detect if the movement is stuck, exit if stuck.
06. Sprint (2.5s cd).
07. Detect if the W button is released and the W button is pressed.
08. Test readiness to end.
09. Print log.
10. Move camera towards BP direction.

## Function parameters

### TMC

```python
def set_parameter(self,
              MODE:str = None,
              target_posi:list = None,
              path_dict:dict = None,
              stop_rule:int = None,
              is_tp:bool = None,
              to_next_posi_offset:float = None,
              special_keys_posi_offset:float = None,
              reaction_to_enemy:str = None,
              tp_type:list = None,
              is_reinit:bool = None,
              is_precise_arrival:bool = None,
              stop_offset = None,
              is_auto_pickup:bool = None):
"""设置参数，如果不填则使用上次的设置。

Args:
    MODE (str, optional): 选择移动模式。可选为'AUTO'自动移动或'PATH'沿路径移动. Defaults to None.
    target_posi (list, optional): 目标坐标。TianLi格式. Defaults to None.
    path_dict (dict, optional): 路径字典。PATH模式时必填. Defaults to None.
    stop_rule (int, optional): 停止条件. Defaults to None.
    is_tp (bool, optional): 是否在移动前TP. Defaults to None.
    to_next_posi_offset (float, optional): 到下一个posi的offset。一般无需设置. Defaults to None.
    special_keys_posi_offset (float, optional): SK的offset。无需设置. Defaults to None.
    reaction_to_enemy (str, optional): 对敌反应。无效设置. Defaults to None.
    tp_type (list, optional): tp类型。列表可包含`Domain` `Teleporter` `Statue`. Defaults to None.
    is_reinit (bool, optional): 是否重初始化TLPS小地图. Defaults to None.
    is_precise_arrival (bool, optional): 是否需要准确到达移动终点. Defaults to None.
    stop_offset (_type_, optional): 停止范围，小于时停止. Defaults to None.
    is_auto_pickup (bool, optional): 是否自动拾取可采集物. Defaults to None.
"""
```
