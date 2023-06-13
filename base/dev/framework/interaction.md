# 交互核心

## 使用

```python
from source.interaction.interaction_core import itt
```

在全局只能存在一个itt变量。

## 方法

itt.appear_then_click(ImgIcon|Button|Text) -> bool

如果出现即点击。

可以传入图片（不推荐），按钮和文字类型。

返回：操作是否成功。

- 注意：根据脚本规范，即使该函数返回成功，也不应该依此判定操作成功，而应该额外检测（如检测特征是否存在/消失），防止由于意外情况操作失效。