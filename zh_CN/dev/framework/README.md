## 基本运作模式

GIA使用和Alas类似的运作方式。

由于windows截图速度远快于模拟器，在while循环中，一些等待是必要的。

由于GIA使用多线程运作，在循环中必须加入退出条件识别。

### 例子：在UI密集型操作中

```python
def siw():
    """delay in while."""
    time.sleep(0.1)
def _switch_to_area(self, tp_region):
    while 1:
        siw()
        if self.checkup_stop_func(): return  # in thread
        itt.appear_then_click(asset.ButtonBigmapSwitchMap)
        if not itt.appear(asset.IconUIBigmap):
            break
    if tp_region == "Mondstadt":
        tp_text = asset.MapAreaMD
    elif tp_region == "Liyue":
        tp_text = asset.MapAreaLY
    elif tp_region == "Inazuma":
        tp_text = asset.MapAreaDQ
    elif tp_region == "Sumeru":
        tp_text = asset.MapAreaXM
    else:
        logger.error(t2t("Unknown region"))
    while 1:
        siw()
        if self.checkup_stop_func(): return  # in thread
        itt.appear_then_click(tp_text)
        if itt.appear(asset.IconUIBigmap):
            break
    while 1:
        siw()
        if self.checkup_stop_func(): return  # in thread
        if itt.appear(asset.IconUIBigmap):
            break
        itt.appear_then_click(asset.ButtonBigmapCloseMarkTableInTP)
```

## 基于图片的 assets 管理

手动写坐标会给后期维护带来麻烦，因为没人知道这个坐标是在哪里。它也会大量占据开发者的时间，以至于脚本的规模受限。

```
area = (790, 275, 911, 321)
```

GIA使用变量名标记图片路径。

e.g.:  General/common/ButtonGeneralUseCondensedResin.jpg: 按钮格式图片，General分类，图片名为UseCondensedResin.

- 打开图片即可方便地查看这个区域在哪里，以及这个区域所包含的内容，方便后期维护。
- 设置好 PhotoShop 动作后，制作一张 assets，比手动输入坐标快。
- 可以在 IDE 中使用自动补全。

当参数为空时，GIA会在imgs文件夹下自动查找与当前变量名一致的文件，省去了填写路径的麻烦。

## OCR

GIA使用 PaddleOCR 识别文字。

以识别石油量为例：

```python
OCR_OIL = Digit(OCR_OIL, name='OCR_OIL', letter=(247, 247, 247), threshold=128)
oil = OCR_OIL.ocr(self.device.image)
```

## 注释

使用 Google 注释规范，例如：

```
"""
Re-focus to the center of a grid.

Args:
    tolerance (float): 0 to 0.5. If None, use MAP_GRID_CENTER_TOLERANCE

Returns:
    bool: Map swiped.
"""
```
