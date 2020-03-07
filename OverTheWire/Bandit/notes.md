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

# Level 17 → Level 18
下一关密码在password.new中，且密码所在行是password.old和password.new中唯一修改过的一行，直接使用diff命令查看两个文件区别：
```
diff passwords.new passwords.old -y --suppress-common-lines #-y表示以并列方式显示两文件差异，--suppress-common-lines表示仅显示不同之处
```
即可显示，注意密码位于password.new中即可。
<!-- 下一关用户名bandit18，密码：kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd-->

# Level 18 → Level 19
下一关密码在readme文件中，但由于bandit18用户文件夹中.bashrc文件被修改，直接通过ssh登录会被直接退出，此时无需登录到服务器，直接在ssh命令后添加要执行的命令：
```
ssh bandit18@localhost cat readme #直接在上一关用户bandit17用户下操作
```
即可查看readme文件中的内容，即下一关密码。
<!-- 下一关用户名bandit19，密码：IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x-->

# Level 19 → Level 20
下一关密码位于/etc/bandit_pass文件夹中，但文件权限不够，通过运行当前文件夹下的可执行文件发现这个文件的作用是将euid设置为bandit20用户，即拥有bandit20用户的权限，然后就可以查看密码文件：
```
./bandit20-do cat /etc/bandit_pass/bandit20
```
<!-- 下一关用户名bandit20，密码：GbKksEFF4yrVs6il55v6gwY5aVje5f0j-->

# Level 20 → Level 21
运行当前文件夹下脚本，可连接至我们指定的端口，并读取连接信息，如果接收到本关密码，将会返回下一关密码，首先通过nc开启一个端口：
```
nc -lv -p 1111 #-l表示监听模式，-v显示详情，-p指定端口
```
打开另一个终端运行脚本：
```
./suconnect 1111
```
此时会显示ERROR，因为未接收到本关密码，所以在第一个终端改为运行：
```
echo "GbKksEFF4yrVs6il55v6gwY5aVje5f0j" | nc -lv -p 1111
```
即可在本端接收到下一关密码。
<!-- 下一关用户名bandit21，密码：gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr-->

# Level 21 → Level 22
查看/etc/cron.d/中的文件，了解什么程序正在计划运行：
```
ls /etc/cron.d/
cat /etc/cron.d/cronjob_bandit22
```
通过观察计划内容发现每分钟都在运行/usr/bin/cronjob_bandit22.sh，查看其内容：
```
cat /usr/bin/cronjob_bandit22.sh
```
发现此脚本试图将下一关密码发到/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv文件中，查看其内容：
```
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
```
即可得到下一关密码。
<!-- 下一关用户名bandit22，密码：Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI-->

# Level 22 → Level 23
前几步和上一关一样，查看/etc/cron.d/cronjob_bandit23计划的内容，然后查看/usr/bin/cronjob_bandit23.sh内容，发现此脚本的意思是将下一关密码导入/tmp/$mytarget文件夹中，其中mytarget=$(echo I am user $myname | md5sum | cut -d ' '  -f 1)，而myname=$(whoami)，此时myname的值为当前用户即bandit22。最初想法是修改cronjob_bandit23.sh内容，直接把myname的值改为bandit23，但由于没有读取/etc/bandit_pass/bandit23的权限无法运行脚本，只能单独运行：
```
echo I am user bandit23 | md5sum | cut -d ' '  -f 1
```
来计算mytarget的值，得到8ca319486bfbbc3663ea0fbe81326349，所以通过：
```
cat /tmp/8ca319486bfbbc3663ea0fbe81326349
```
查看其内容即可得到下一关密码。
<!-- 下一关用户名bandit23，密码：jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n-->

# Level 23 → Level 24
前几步和上一关一样，查看/etc/cron.d/cronjob_bandit24计划的内容，然后查看/usr/bin/cronjob_bandit24.sh内容，发现此脚本的作用是每分钟删除一次/var/spool/bandit24/文件夹下的所有文件，猜测是要编写脚本然后放到这个目录下执行，但由于这个目录每分钟都会被清除一次，所以在/tmp目录下编辑好脚本后复制到/var/spool/bandit24/文件夹下：
```
mkdir /tmp/getpass11111
cd /tmp/getpass11111
vim getpass.sh
```
其中getpass.sh内容为：
```
#!/bin/bash
cat /etc/bandit_pass/bandit24 >>  /tmp/getpass11111/pass
```
然后把文件复制到/var/spool/bandit24/文件夹下等待执行即可
```
cp getpass.sh /var/spool/bandit24/
chmod 777 /var/spool/bandit24/getpass.sh #此处赋权是因为将脚本复制到该文件夹后的权限不足以作为bandit24用户运行。此步操作可能会报错文件不存在，是因为定时计划的每一分钟清空文件夹操作已进行，重复上一步即可
```
最后通过：
```
cat pass
```
查看密码，此处可能报错文件不存在，是因为脚本还未被运行，等待一分钟定时计划运行即可。
<!-- 下一关用户名bandit24，密码：UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ-->

# Level 24 → Level 25
本关需要构造“上一关密码+空格+4位数密码”的字符串发送到本机30002端口，只有发送的内容正确才能得到回传的下一关密码，这一关的重点在于遍历所有4位数密码的可能性，然后逐一尝试发送，也就是进行暴力破解。一开始的思路是：
```
#! /bin/bash
a=1000 #无法遍历前1000种可能，因为整数无法在前面补0
while [ "$a" -lt 10000 ]; do
	echo "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ "$a | nc localhost 30002 >> 1.txt #将输出结果导出到文件中，最后从文件中读取数据，无需时刻观察
	a=$(($a+1))
done
```
这个方法的问题有两个，第一个就是无法遍历前1000种可能，而真正的密码可能就在其中；第二个就是等待时间过长，即使在nc中使用-w1来限制1秒的自动超时时间，完整遍历9000种可能性也需要150分钟，不加参数等待自动超时将更久。为此做了如下修改：
```
#!/bin/bash
a="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for i in {0..9}{0..9}{0..9}{0..9} #可以遍历所有10000种可能性
do
echo $a' '$i >> dic.txt #生成了一个密码字典
done
cat dic.txt | nc localhost 30002 >> 2.txt #通过遍历字典的方式能极大程度缩短时间
tail -n 5 2.txt #发送正确的密码后会回传下一关密码并自动退出，因此查看输出结果最后几行内容即可
```
<!-- 下一关用户名bandit25，密码：uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG-->

# Level 25 → Level 26
下一关的用户bandit26的shell不是/bin/bash，直接通过ls发现目录下有一个ssh私钥，通过：
```
ssh bandit26@localhost -i bandit26.sshkey #参见Level13
```
会发现直接退出，查看一下bandit26的shell是什么：
```
cat /etc/passwd | grep "bandit26"
```
发现bandit26用户的shell是/usr/bin/showtext，通过cat看看这是什么，发现通过more命令运行了一个文本，运行完以后就通过exit0退出了。more命令的特性是如果一个页面显示不完整会中断，用户可自行翻页，与此同时按v即可进入vi模式，此时输入：
```
:r /etc/bandit_pass/bandit26 #vi模式下:r表示进入取代模式，成功运行后光标所在位置的字符会被取代，这里使用bandit26用户的密码来取代
```
即可显示bandit26用户的密码。关键点在于让more命令显示的文本无法完全显示，通过之前的登录失败界面可以发现more命令显示的文本（bandit26字符画）有6行，尝试将终端高度缩到6行即可成功中断。
<!-- 下一关用户名bandit26，密码：5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z-->

# Level 26 → Level 27
首先和上一关一样中断more命令并进入vi模式，通过：
```
:set shell sh=/bin/sh #设置想要使用的shell
:sh #进入当前shell
ls -l#查看当前目录下的文件，发现有一个bandit27-do文件的suid为bandit27
file bandit27-do #是一个可执行文件
./bandit27-do cat /etc/bandit_pass/bandit27 #参见Level19
```
<!-- 下一关用户名bandit27，密码：3ba3118a22e93127a4ed485be72ef5ea-->

# Level 27 → Level 28
从本关起是git相关内容，使用bandit27用户登入后通过：
```
mkdir /tmp/110111
cd /tmp/110111
git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
```
来克隆目标地址的内容即可，然后进入repo文件夹，查看README内容即可。
<!-- 下一关用户名bandit28，密码：0ef186ac70e04ea33b4c1853d2526fa2-->

# Level 28 → Level 29
首先和上一关一样clone目标地址内容，进入repo文件夹后查看README.md的内容，发现密码未显示，通过：
```
git log
```
查看提交历史，发现add missing data这条commit比较可疑，查看修改记录：
```
git diff 186a1038cc54d1358d42d468cdc8e3cc28a93fcb
```
发现被修改的下一关密码。
<!-- 下一关用户名bandit29，密码：bbc96594b4e001778eee9975372716b2-->

# Level 29 → Level 30
首先和上一关一样clone目标地址内容，进入repo文件夹后查看README.md的内容，根据提示猜测密码可能不在这个分支，通过：
```
git branch -a #-a表示查看全部分支
```
查看全部分支，发现还存在dev和sploits-dev分支，切换到dev分支看看：
```
git checkout -b  dev origin/dev #新建一个dev分支，内容从origin/dev粘过来
ls #发现目录下有READ.md和code文件夹
cat READ.md #里面就有密码
```
<!-- 下一关用户名bandit30，密码：5b90576bedb2cc04c86a9e924ce42faf-->

# Level 30 → Level 31
首先和上一关一样clone目标地址内容，进入repo文件夹后查看README.md的内容，发现里面是空的，查看分支和历史也没有信息，通过：
```
git show-ref #显示本地存储库中可用的引用以及关联的提交ID
```
发现最后一行比较可疑，查看：
```
git show f17132340e8ee6c159e0a4a6bc6f80e1da3b1aea
```
即可得到密码。
<!-- 下一关用户名bandit31，密码：47e603bb428404d265f59c42920d81e5-->

# Level 31 → Level 32
首先和上一关一样clone目标地址内容，进入repo文件夹后查看README.md的内容，发现本关需要提交key.txt，内容为'May I come in?'，首先写入文件：
```
echo 'May I come in?' >> key.txt
```
通过ls -a会发现文件夹下有一个.gitignore文件，Git就会自动忽略这个文件里面提到的文件，查看内容发现是*.txt，意味着我们无法直接提交key.txt，所以移除后再提交：
```
git rm .gitignore
git add key.txt
git commit #之后会进入编辑器修改commit提交的信息，修改完内容后保存退出
git push
```
即可看到返回内容里的密码。
<!-- 下一关用户名bandit32，密码：56a9bf19c63d650ce78e6ec0354ee45e-->

# Level 32 → Level 33
进入之后发现不知道是在什么环境下，随便输入几个指令发现都被转换成了大写，直接输入$0获得shell，此时通过whoami发现我们已经是bandit33用户（通过ls -l可以发现脚本运行后权限为bandit33，原理同Level19），直接cat查看/etc/bandit_pass/bandit33就能获得密码。
<!-- 下一关用户名bandit33，密码：c9c3199ddf4121b10cf581a98d51caee-->

# Level 33 → Level 34
暂时没有啦～
