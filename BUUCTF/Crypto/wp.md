# 注意事项：
注意规范flag格式为flag{}，有的其他比赛找来的题flag头是各自比赛的名字，注意修改。  
先看题目名称和题目内容，可能都是有用的线索。但不是所有题目都提示了flag内容的格式，所以解出的答案看着很对但提交显示不正确的时候试试大小写字母转换，空格或下划线连接符转换
# MD5
直接扔到md5解密在线网站（本次使用https://www.cmd5.com ）解密即可得到flag：flag{admin1}
# Url编码
直接扔到url解码在线网站（本次使用http://www.bejson.com/enc/urlencode/ ）解密即可得到flag：flag{and 1=1}
# 看我回旋踢
根据题目名称猜想是凯撒密码，直接扔到凯撒密码在线网站（本次使用https://www.ctftools.com/down/ 中的凯撒密码模块）列出所有组合即可得到flag：flag{5cd1004d-86a5-46d8-b720-beb5ba0417e1}
# 一眼就解密
根据密文最后的等于号猜想是base64加密，直接扔到base64解码在线网站（本次使用https://base64.supfree.net/ ）解密即可得到flag：flag{THE_FLAG_OF_THIS_STRING}
# 摩丝
根据题目名称和密文内容猜想是摩斯电码，直接扔到摩斯电码在线网站（本次使用https://www.ctftools.com/down/ 中的摩斯电码模块），修改点的内容为“.“和字母间隔为空格后即可得到flag：flag{ILOVEYOU}
# [BJDCTF 2nd]签到-y1ng
根据密文最后的两个等于号猜想是base64加密，直接扔到base64解码在线网站（本次使用https://base64.supfree.net/ ）解密即可得到flag：flag{W3lc0me_T0_BJDCTF}
# password
根据密文格式共10位直接猜密码为名字首字母+生日，得到flag：flag{zs19900315}
# 变异凯撒
根据题目名称可知此题并非简单的凯撒密码，通过对比密文前五位和“flag{”的ascii码可以发现位移依次为5、6、7、8、9，推测密文的偏移量为逐位+1。此处需要自己编写脚本实现解密，本次使用python3，代码内容为：

```
enc = "afZ_r9VYfScOeO_UL^RWUc"	#密文
n = 5	#初始偏移量为5位
for i in enc:
    print(chr(ord(i)+n),end='')	#先通过ord函数计算原始密文中每个字符的ascii码，加上偏移量后再通过chr函数转换成字符，结尾不换行，让结果输出到一行
    n += 1	#偏移量逐位+1
```

直接看输出内容即可得到flag：flag{Caesar_variation}
# 篱笆墙的影子
根据题目名称猜测是栅栏密码，直接扔到栅栏密码在线网站（本次使用https://www.ctftools.com/down/ 中的栅栏密码模块），列举解密即可得到flag：flag{wethinkwehavetheflag}
# 大帝的密码武器
根据题目名称和题目描述可以猜出是凯撒密码，直接扔到凯撒密码在线网站（本次使用https://www.ctftools.com/down/ 中的凯撒密码模块）列出所有组合可以看出密文在偏移13位时得到有意义的单词“SECURITY”，用同样的加密向量加密“ComeChina”，即可得到flag{PbzrPuvan}