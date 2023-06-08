# 配置文档书写指南

## 命名格式

The name is generally the name of the target document plus the suffix `{language}.jsondoc`.

For example, the document name corresponding to `auto_domain.json` should be `auto_domain.json.zh_CN.jsondoc`.

## Storage Location

It should be stored in the same directory as the corresponding configuration according to the naming convention.

## Translation

Write the translation corresponding to the key into the doc. For example:

```yaml
{
  domain_times: 
    doc: 1


  fast_mode:
    doc: true


  isLiYueDomain: 
    doc: false,
  resin: 
    doc: 20
}
```

## Selection Box

以前想过这个问题，不过觉得应该可以不用就没写，这次看来是必须写了……

Same as above, the selection box only needs to add an item named `select_items` in yaml.

For example:

```yaml

  itemname: 
    select_items: [
      甜甜花 - 蒙德,
      霓裳花 - 璃月,
      鸣草 - 稻妻
    ],
    doc: 物品名

```

## Special Key

Flags for executing special methods.

## Others

- If you think there are some unnecessary translations, you can delete the key-value pair, and the program will automatically use the configured value as the title.
- **Please do not write unparseable yaml documents!!!**
