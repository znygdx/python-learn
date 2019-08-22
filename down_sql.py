#coding=utf-8
from ftplib import FTP
import os
import re
import sys
def download_sql(f,localfile):
    bufsize = 1024
    file_handle = open(localfile,'wb')
    f.retrbinary("RETR " + localfile, file_handle.write, bufsize)
    file_handle.close()
    print('done')
#本地sql
local_path = os.getcwd()
list_local = os.listdir(local_path)

dir = input('请输入你想下载的脚本，如果是修订10，请输入10.2:')
f = FTP('10.12.12.9')
f.login('','')
list_to_find = f.nlst()
list_to_findnew = list(filter(lambda x:re.match('iTap'+dir,x) != None,list_to_find))
new_dir = list_to_findnew[-1]
print(new_dir)
f.cwd(new_dir+'/iTapSQL')
list_ftp= f.nlst()

#获取要下载的脚本
list_dif = list(set(list_ftp)-set(list_local))
list_ftp.reverse()

for i in list_ftp:
   if i in list_dif:
        download_sql(f,i)



