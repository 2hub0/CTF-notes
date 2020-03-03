https://overthewire.org/wargames/bandit/  
  
# Level 0
首先根据提示使用ssh登录bandit.labs.overthewire.org(此处可以先通过ping获取服务器ip：176.9.9.172，然后通过ip登录，也可直接通过url登录)，端口为2220。其中用户名为bandit0，密码也为bandit0。通过：  
```
ssh bandit0@bandit.labs.overthewire.org -p 2220
```
连接服务器，然后输入密码，即可登录到服务器。

# Level 0 → Level 1
查看home文件夹下的“readme”文件即可获取下一关密码，直接输入ls查看当前目录下的文件，发现readme文件就在当前目录下，通过：
```
cat readme
```
查看“readme”文件内容即可。
<!-- 下一关用户名bandit1，密码：boJ9jbbUNNfktd78OOpsqOltutMc3MY1-->


# Level 1 → Level 2
查看home文件夹下“-”文件即可获取下一关密码，直接输入ls查看当前目录下的文件，发现-文件就在当前目录下，通过：
```
cat ./-
```
查看“-”文件内容即可。此处的关键在于读取虚线文件的方法。
<!-- 下一关用户名bandit2，密码：CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9-->

# Level 2 → Level 3
查看home文件夹下的“spaces in this filename”文件即可获取下一关密码，直接输入ls查看当前目录下的文件，发现“spaces in this filename”文件就在当前目录下，通过：
```
cat spaces\ in\ this\ filename
```
查看“spaces in this filename”文件内容即可。此处的关键在于通过“\”来转义文件名中的空格，如果输入完“cat s”后直接按Tab自动补齐文件名，反斜杠会自动添加。
<!-- 下一关用户名bandit3，密码：UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK-->

# Level 3 → Level 4
查看inhere文件夹下隐藏文件即可获取下一关密码，直接输入ls查看当前目录下的文件，发现inhere文件夹就在当前目录下，通过：
```
cd inhere
```
进入inhere文件夹，通过：
```
ls -a
```
查看当前文件夹下全部文件，包含文件名开头为“.”的隐藏文件，发现“.hidden”文件，通过：
```
cat .hidden
```
查看“.hidden”文件内容即可。
<!-- 下一关用户名bandit4，密码：pIwrPrtPN36QITSp3EQaw936yaFoFgAB-->

# Level 4 → Level 5
查看inhere文件夹下“人能读的”文件即可获取下一关密码，直接输入ls查看当前目录下的文件，发现inhere文件夹就在当前目录下，进入inhere文件夹后，通过ls
发现当前文件夹下有10个文件，依次通过：
```
cat ./-file00
cat ./-file01
...
```
遍历查看十个文件内容，发现仅-file07文件内容可读，即为密码。
<!-- 下一关用户名bandit5，密码：koReBOKuIDDepwhWk7jZC0RTdopnAYKh-->

# Level 5 → Level 6
查看inhere文件夹下“人能读的”、大小为1033bytes、不可执行的文件即可获取下一关密码，直接通过指定文件大小进行全盘搜索即可：
```
find / -size 1033c
```
其中-size表示指定文件大小，可为一个数或一个范围，c表示单位为字节，发现符合条件的文件路径/home/bandit5/inhere/maybehere07/.file2，通过cat查看即可。
<!-- 下一关用户名bandit6，密码：DXjZPULLxYr17uwoI01bNLQbtFemEgo7-->

# Level 6 → Level 7
查看服务器上某处文件夹下“所有者为bandit7、所属组为bandit6、大小为33bytes“的文件即可获取下一关密码，直接通过这三个条件进行全盘搜索即可：
```
find / -group bandit6 -user bandit7 -size 33c
```
其中-group表示文件所属组，-user表示文件所属用户，现符合条件的文件路径/var/lib/dpkg/info/bandit7.password，通过cat查看即可。
<!-- 下一关用户名bandit7，密码：HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs-->

# Level 7 → Level 8
查看文件data.txt，其中下一关密码位于“millionth”单词边上，通过cat和grep命令组合限制输出内容：
```
cat data.txt | grep millionth
```
其中|起管道作用，将前一个命令的结果输出到第二个命令中，grep命令用来匹配格式，并把匹配的行打印出来，即可看到密码。
<!-- 下一关用户名bandit8，密码：cvX2JJa4CFALtqS87jk27qwqGhBM9plV-->

# Level 8 → Level 9
查看文件data.txt，其中下一关密码只出现了一行，uniq命令用于检查及删除文本文件中重复出现的行，通常与sort连用，通过：
```
sort data.txt | uniq -u
```
首先使用sort进行排序，将data.txt文件中相同的内容放到一起，因为uniq只能删除连续出现的重复行，-u表示仅显示出一次的行列，即可得到密码。
<!-- 下一关用户名bandit9，密码：UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR-->

# Level 9 → Level 10
查看文件data.txt，其中下一关密码混在一串“人能读的”字符串中，以若干个“=”开头，通过strings方法只显示可打印的字符：
```
strings data.txt | grep =========
```
即可得到密码。
<!-- 下一关用户名bandit10，密码：truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk-->

# Level 10 → Level 11
查看文件data.txt，其中下一关密码是base64编码后的数据，通过base64方法解码：
```
cat data.txt | base64 -d
```
其中-d选项表示base64解码，即可得到密码。
<!-- 下一关用户名bandit11，密码：IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR-->

# Level 11 → Level 12
查看文件data.txt，其内容是ROT13(回转13位)加密后的下一关密码，使用tr方法进行内容替换：
```
cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
```
通过把data.txt中的内容一一替换为移位13位以后的内容即可解码。
<!-- 下一关用户名bandit12，密码：5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu-->

# Level 12 → Level 13
data.txt是一个被反复压缩后的文件的十六进制编码，首先将data.txt文件复制到/tmp/test文件夹下方便后续操作：
```
cp data.txt /tmp/test/data.txt
```
首先通过xxd方法的-r选项将data.txt从十六进制编码转换成二进制编码文件data.bin：
```
xxd -r data.txt data.bin
```
此后循环如下过程：
```
file data.bin  #第一步：查看文件类型，是gzip、bzip2、tar压缩中的哪一种
mv data.bin data.gz  #第二步：将文件后缀改为对应压缩文件的后缀，如果是gzip压缩则后缀改为.gz，bzip2则改为.bz，tar则改为.tar
gzip -d data.gz  #第三步：gzip解压
bzip2 -d data.bz  #第三步：bzip2解压
tar -xvf data.tar  #第三步：tar解压
#将解压后的文件带回第一步继续下一个循环，直到最后通过file命令查看到的文件类型为：ASCII text，通过cat查看即可
```
<!-- 下一关用户名bandit13，密码：8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL-->

# Level 13 → Level 14
从本关登录到下一关的方式不是通过密码，而是通过SSH key登录，通过ls和cat发现当前目录下存有私钥文件，通过：
```
ssh bandit14@localhost -i sshkey.private
```
就可以使用bandit14用户身份登录。

# Level 14 → Level 15
使用bandit14用户登录后根据上一关提示，通过cat从/etc/bandit_pass/bandit14中得到一串密码，通过：
```
nc localhost 30000
```
连接本地30000端口，然后输入刚刚得到的一串密码，得到下一关密码。
<!-- 下一关用户名bandit15，密码：BfMYroe26WYalil77FoDi9qh59eK5xNr-->

# Level 15 → Level 16
使用SSL连接到本机30001端口并发送本关登录密码即可得到下一关密码：
```
openssl s_client -connect localhost:30001
```
<!-- 下一关用户名bandit16，密码：cluFn7wTiGryunymYOu4RcffSxQluehd-->

# Level 16 → Level 17
首先使用nmap扫描本机31000-32000端口，以确认哪个符合要求：
```
nmap -sV -v  localhost -p 31000-32000 #-p指定端口，-sV探测服务版本
```
结果显示有两个端口开着，31518和31790都使用SSL连接，但31580服务显示为“echo”，猜测为题目中所说的返回无用信息的端口。通过SSL连接31790端口，并将包含私钥的输出结果保存：
```
mkdir /tmp/test #在tmp文件夹下自己新建一个文件夹才有写文件权限
openssl s_client -connect localhost:31790 | tee /tmp/test/1.txt
```
然后编辑输出文件，删掉私钥前后的无用信息，并通过SSH连接：
```
vi 1.txt #删掉无用信息
chmod 600 1.txt #需要修改文件权限，否则会报错
ssh -i 1.txt bandit17@localhost
cat /etc/bandit_pass/bandit17 #以bandit17用户登录后可查看密码
```
<!-- 下一关用户名bandit17，密码：xLYVMN9WE5zQ5vHacb0sZEVqbrp7nBTn-->
