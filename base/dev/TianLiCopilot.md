# TianLiCopilot 天理自动驾驶

TLC(TianLiCopilot)基于TeyvatMoveFlow(TMF)提瓦特移动控制流。  
TLC使用[TLPS](./TianLiPositioningSystem)定位.

## 简介
TLC包含2种模式:`AUTO`与`PATH`.  
AUTO模式下,程序将会结合[TLN](./TianLiPositioningSystem)朝目标前进.  
PATH模式下,程序将会使用[TLPP](./TianLiPositioningPath.md)文件沿路线行驶.

## 工作原理

### AUTO模式

AUTO模式会朝着目标坐标方向直行。在走路状态下每1.6s连按2次空格。  
如果启用了TLN(TianLi Positioning Navigator),会使用TLN进行辅助导航。  
[TLPS&TLN](./TianLiPositioningSystem.md)

### PATH模式

PATH模式会沿着坐标前进。在循环过程中，执行以下3个步骤：

1. 朝着break position（转折点）前进。距离BP小于规定的offset即切换到下一个BP，直到没有更多BP。
2. 自动识别当前的position，并检测motion并处理。
3. 如果当前距离距离吸附点小于允许吸附距离，开始向目标吸附点移动
4. 自动拾取(若启用)
5. 检测移动是否卡住，卡住就退出
6. 冲刺(2.5s cd)
7. 检测W按键是否松开并按下W按键
8. 检测是否准备结束。若是，检测是否需要精确结束。若是，向终点移动(offset=1)
9. 打印日志
10. 移动视角朝向BP方向

## 函数参数
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


