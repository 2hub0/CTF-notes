a = open('/44aaac34ab1449fe8df001fcb0ec4e24.txt','r')
b = a.readline()
c = ""
d = ""
for i in b:
    if i == '0':
        i = '.'
    elif i == '1':
        i = '-'
    c = c + i
#Morse字典
dict_morse = {'.-': 'A',
        '-...': 'B',
        '-.-.': 'C',
        '-..':'D',
        '.':'E',
        '..-.':'F',
        '--.': 'G',
        '....': 'H',
        '..': 'I',
        '.---':'J',
        '-.-': 'K',
        '.-..': 'L',
        '--': 'M',
        '-.': 'N',
        '---': 'O',
        '.--.': 'P',
        '--.-': 'Q',
        '.-.': 'R',
        '...': 'S',
        '-': 'T',
        '..-': 'U',
        '...-': 'V',
        '.--': 'W',
        '-..-': 'X',
        '-.--': 'Y',
        '--..': 'Z',
        '.----': '1',
        '..---': '2',
        '...--': '3',
        '....-': '4',
        '.....': '5',
        '-....': '6',
        '--...': '7',
        '---..': '8',
        '----.': '9',
        '-----': '0'
        }
c = c.split('/')
for i in c:
    if dict_morse.get(i): #通过dict_morse对象的get()方法判断键是否存在
        d = d + dict_morse[i].lower()
    else: #无关内容不解密
        d = d + i
d = d[50:] #删除无关内容
e = [] #密文列表
f = ""
num = 0
for i in d:
    if num!=0 and num % 5 == 0:
        e = e + [f]
        f=""
    f = f + i
    num=num+1
#培根密码字典
dict_bacon={'aaaaa':'a','aaaab':'b','aaaba':'c','aaabb':'d','aabaa':'e','aabab':'f','aabba':'g',
    'aabbb':'h','abaaa':'i','abaab':'j','ababa':'k','ababb':'l','abbaa':'m','abbab':'n',
    'abbba':'o','abbbb':'p','baaaa':'q','baaab':'r','baaba':'s','baabb':'t','babaa':'u',
    'babab':'v','babba':'w','babbb':'x','bbaaa':'y','bbaab':'z'}
for i in e:
    print(dict_bacon[i],end='')
