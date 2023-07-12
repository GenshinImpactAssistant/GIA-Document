# Manager

位置：source/manager

manager负责管理程序的所有资源，包括图片和文字。

# 命名格式

使用开头大写。

图片路径格式：
./assets/imgs/Windows/\[Image-classification\]/\[zh_CN|en_US|common\]/img_name
图片文件名（img_name）使用以下格式：
\[Area | Button | Icon\]\[Image-classification\]\[Image-name\].jpg

e.g.:

- General/common/ButtonGeneralUseCondensedResin.jpg: 按钮格式图片，General分类，图片名为UseCondensedResin.

## ImgIcon

位置：source/manager/img_template

### 调用

```python
ImgIcon(path=None,
        name=None,
        is_bbg=None,
        alpha=None,
        bbg_posi=None,
        cap_posi = None,
        jpgmode=2,
        threshold=0.91,
        win_page = 'all',
        win_text = None,
        offset = 0,
        print_log = LOG_NONE)
```

1. path：文件路径\
   如果不填，按照变量名生成路径。\
   e.g. IconCommissionCommissionIcon = ImgIcon():查找IconCommissionCommissionIcon.jpg的路径并自动填写。
2. name：名称\
   如果不填，按照变量名生成名称。
3. is_bbg：是否为黑色背景的挖空图片\
   如果不填，识别图像分辨率。如果分辨率为1080p则为False，否则为True。
4. cap_posi：截图坐标\
   如果填写，itt只会截取坐标内的图片并进行匹配。
5. threshold：匹配阈值
6. offset：截图范围偏移\
   如果填写，截图区域(cap_posi)将扩大。
7. print_log：日志打印模式\
   有以下选项：LOG_NONE | LOG_WHEN_TRUE | LOG_WHEN_FALSE | LOG_ALL

## Button

Button是ImgIcon的子类，因此ImgIcon的大部分参数可适用于Button。

图片识别时可以使用ImgIcon，需要点击的图片使用Button。

特殊参数：

1. click_offset：点击偏移范围

## Text

肥肠简单

```python
Text(zh='',en='')
```

如果在函数中传参，一般直接传入对象。调用文字的时候使用xxx.text，返回当前语言的文字。

## PosiTemplate

管理坐标。

参数：

1. name：坐标名称。\
   如果不填使用变量名。

2. img_path：图片路径\
   如果填写，根据图片提取坐标（必须为黑色背景挖空图片）。

3. posi：坐标范围（\[left x,left y,right x,right y\]）\
   如果不填，根据图片路径查找对应图片。如果图片路径为空，根据变量名查找图片。

推荐使用图片标记坐标以方便管理。
