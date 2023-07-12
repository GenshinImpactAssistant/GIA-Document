# 交互核心

## Usage

```python
from source.interaction.interaction_core import itt
```

在全局只能存在一个itt变量。默认已创建。

## Methods

1. itt.appear_then_click(ImgIcon|Button|Text) -> bool

   如果出现即点击。

   可以传入图片（不推荐），按钮和文字类型。

   返回：操作是否成功。

   - 注意：根据规范，即使该函数返回成功，也不应该依此判定操作成功，而应该额外检测（如检测特征是否存在/消失），防止由于意外情况操作失效。

2. itt.appear(ImgIcon|Text) -> bool

   对象是否存在。存在返回True，否则返回False。

   检测阈值在对象创建时设定。
