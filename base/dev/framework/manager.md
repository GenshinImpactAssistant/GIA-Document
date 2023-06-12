# Manager

位置：source/manager

manager负责管理程序的所有资源，包括图片和文字。

# 命名格式
使用开头大写。

图片路径格式：
./assets/imgs/Windows/[Image-classification]/[zh_CN|en_US|common]/img_name
图片文件名（img_name）使用以下格式：
[Area|Button|Icon][Image-classification][Image-name].jpg

e.g.:
- General/common/ButtonGeneralUseCondensedResin.jpg: 按钮格式图片，General分类，图片名为UseCondensedResin.


## ImgIcon

位置：source/manager/img_template

### 调用
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

1. path：文件路径
    如果不填，按照变量名生成路径。  
    e.g. IconCommissionCommissionIcon = ImgIcon():查找IconCommissionCommissionIcon.jpg的路径并自动填写。
2. name：名称
    如果不填，按照变量名生成名称。
3. is_bbg：是否为黑色背景的挖空图片
    如果不填，识别图像分辨率。如果分辨率为1080p则为False，否则为True。
4.  cap_posi：截图坐标
    如果填写，itt只会截取坐标内的图片并进行匹配。
5. threshold：匹配阈值
6. offset：截图范围偏移
    如果填写，截图区域(cap_posi)将扩大。
7. print_log：日志打印模式
    有以下选项：LOG_NONE | LOG_WHEN_TRUE | LOG_WHEN_FALSE | LOG_ALL

## Button

Button是ImgIcon的子类，因此ImgIcon的大部分参数可适用于Button。  
特殊参数：
1. click_offset：点击偏移范围

## Text

## PosiTemplate