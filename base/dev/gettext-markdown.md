# Gettext Markdown

GIA使用`py-gettext-markdown`的快速命令。

## Generate pot files
```powershell
cd py-gettext-markdown;python gettext-markdown.py pot -l zh_CN,en_US -f ../doc -c true;cd ../;
```

## Generate markdowns
```powershell
cd py-gettext-markdown;python gettext-markdown.py md -l zh_CN,en_US -f ../doc;cd ../;
```