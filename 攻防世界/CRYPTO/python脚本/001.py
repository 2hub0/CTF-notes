import base64
a = open('/af681321af224387a21c72456530989e.txt','r')
b = a.readline()
c = base64.b64decode(b)
print (str(c,'utf-8'))