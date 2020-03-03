https://overthewire.org/wargames/bandit/  
  
# Level 0
首先根据提示使用ssh登录bandit.labs.overthewire.org(此处可以先通过ping获取服务器ip，然后通过ip登录，也可直接通过url登录)，端口为2220。其中用户名为bandit0，密码也为bandit0。通过：  
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
