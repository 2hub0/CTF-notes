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
# 凯撒？替换？呵呵！
此题并非简单凯撒密码，每个字母的移位数都不同，所以直接爆破（本次使用https://quipqiup.com/ 进行词频爆破），加上已知条件MTHJ=flag，爆破出的第一条结果即是flag，注意转换成小写字母并删除空格，flag{substitutioncipherdecryptionisalwayseasyjustlikeapieceofcake}
# 信息化时代的步伐
根据题目描述，flag内容是中文，通过中文电码在线网站(本次使用http://code.mcdvisa.com/ 中的电码反查中文)可解出明文，flag{计算机要从娃娃抓起}
# old-fashion
观察密文为长文本，直接进行词频爆破（本次使用https://quipqiup.com/ 进行词频爆破），从爆破出的内容末尾部分可以看到flag：flag{n1_2hen-d3_hu1-mi-ma_a}
# [BJDCTF 2nd]Y1nglish-y1ng
观察密文为长文本，直接进行词频爆破（本次使用https://quipqiup.com/ 进行词频爆破），从爆破出的内容末尾部分可以看到flag，根据题目提示把最后一个字母从y改成k：flag{pyth0n_Brut3_f0rc3_oR_quipquip_AI_Cr4ck}
# 萌萌哒的八戒
通过题目名称想到猪圈密码，使用在线网站解密（本次使用http://ctf.ssleye.com/pigpen.html ），规范flag格式后得到flag ：flag{whenthepigwanttoeat}
# 世上无难事
观察密文为长文本，直接进行词频爆破（本次使用https://quipqiup.com/ 进行词频爆破），从爆破出的内容末尾部分可以看到flag：flag{640e11012805f211b0ab24ff02a1ed09}
# rot
根据题目名称想到凯撒密码，但移位个数未知，遂爆破之：

```
enc = [83,89,78,84,45,86,96,45,115,121,110,116,136,132,132,132,108,128,117,118,134,110,123,111,110,127,108,112,124,122,108,118,128,108,131,114,127,134,108,116,124,124,113,108,76,76,76,76,138,23,90,81,66,71,64,69,114,65,112,64,66,63,69,61,70,114,62,66,61,62,69,67,70,63,61,110,110,112,64,68,62,70,61,112,111,112]
for i in range (-127,127):
    for j in enc:
        if (i+j>47) & (i+j<127):
            print(chr(i+j),end='')
    print ()
```

从输出结果中观察到其中一行内容为：

```
FLAGISflag{www_shiyanbar_com_is_very_good_????}MD5:38e4c352809e150186920aac37190cbc
```

其中flag内容似乎还有4位未知，但给出了MD5值，所以再爆破一下这4位的内容并计算flag串的MD5值，只要值相同就得到了flag：

```
import hashlib
flag = "flag{www_shiyanbar_com_is_very_good_"
for a in range(32,126): #只选取了可读字符的ASCII码范围，下同
    for b in range(32,126):
        for c in range(32,126):
            for d in range(32,126):
                key = ""
                key += chr(a) + chr(b) + chr(c) + chr(d)
                if (hashlib.md5((flag+key+"}").encode('utf-8')).hexdigest()) == "38e4c352809e150186920aac37190cbc":
                    print (flag+key+"}")
```

得到flag：flag{www_shiyanbar_com_is_very_good_@8Mu}
# [MRCTF2020]vigenere
根据题目名称想到维吉尼亚密码，使用在线网站解密（本次使用https://guballa.de/vigenere-solver ），查看题目提供的python文件可以看到key的长度为5-10，将语言改为英文，解密，即可在最后一段看到flag：flag{vigenere_crypto_crack_man}
# [AFCTF2018]Vigenère
根据题目名称想到维吉尼亚密码，使用在线网站解密（本次使用https://guballa.de/vigenere-solver ），根据题目提供的c语言文件无法得知key的长度，使用网站默认长度3-30即可，将语言改为英文，解密，即可在中间部分看到flag：flag{Whooooooo_U_Gotcha!}