a = open('/9f08657b76274fa3b64a8e506ba98c48.txt','r')
b = a.readline()
n = 12 #Caesar密码偏移量
for i in b:
    if i == '{' or i == '}' or i == '_': #过滤特殊字符
        print (i,end='')
    else:
        #ord函数将字符转换为十进制ascii码，chr函数将十进制ascii码转换为字符
        #由于小写字母a的ascii码为97，所以将其转换为0即可完成取余数操作
        print(chr((ord(i)-97-n)%26+97),end='')