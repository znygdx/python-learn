# coding=utf-8
from ftplib import FTP
import time
import os
import re
import sys
import zipfile
import shutil
from xml.dom.minidom import Document
from pywinauto.application import Application

#获取执行文件绝对路径
path = os.path.abspath(sys.argv[0])
path_dir = path.split('\\')[:-1]
path_dir_finally = '\\'.join(path_dir)

f = FTP("10.12.12.9")
f.login("", "")

# 选择进入哪个文件夹的交互流程
while True:
    dir_name = input("输入要进入的目录，如果要进入iTap32.2就输入32.2\n请输入：")
    try:
        f.cwd("iTap" + dir_name)
        break
    except:
        print("输错了，重新输入")

# 获取文件夹所有服务的名称列表
zipfilename1 = f.nlst()
zipfilename = sorted(zipfilename1, key=lambda i: len(i))
zipfilename.reverse()
# 列表转换成字符串，方便正则表达式筛选
s = " ".join(zipfilename)

# 筛选最新服务的函数，返回获取到的最新服务名称，列表形式
def find(*args):
    total_list = []
    result = ""
    for i in args:
        # 使用非贪婪匹配
        total_list_init = re.compile(i + dir_name + ".*?zip").findall(s)
        total_list = total_list_init[:5]
    return total_list


# 运行筛选函数
total_list = find("iTapManager")

# 将列表转换为字典，方便下载时的输入
service_dir = dict(zip([str(i) for i in range(len(total_list))], [i for i in total_list]))

# 下载函数，包括解压替换
def download(f, name):
    bufsize = 1024
    file_handle = open(name, "wb")
    f.retrbinary("RETR %s" % name, file_handle.write, bufsize)
    file_handle.close()
    print(name + "下载完成\n-------------------------------------------------")

# 下载时的交互流程
while True:
    service_name = input("输入要下载的服务编号，对应关系如下：\n%s\n请输入：" % str(service_dir).replace(",", "\n"))
    if service_name is "q":
        break

    elif service_name is "a":

        for i in total_list:
            download(f, i)
        break
    elif service_name in service_dir.keys():

        download(f, service_dir[service_name])
        break
    else:
        print("输错了，重新输入\n------------------------------------------------")
#解压文件
myzip = zipfile.ZipFile(path_dir_finally+'\\'+service_dir[service_name])
mystr = myzip.filename.split('\\')[-1].split('zip')
myzip.extractall(mystr[0])
if not os.path.exists(path_dir_finally+'\\'+mystr[0]):
    shutil.move(mystr[0],path_dir_finally)
myzip.close()
os.remove(path_dir_finally+'\\'+service_dir[service_name])
os.chdir(path_dir_finally+'\\'+mystr[0]+'\\'+mystr[0])
if not os.path.exists('ConfigPrivate'):
    os.mkdir('ConfigPrivate')
    os.chdir(path_dir_finally+'\\'+mystr[0]+'\\'+mystr[0]+'\\'+'ConfigPrivate')

#生成Local.xml文档
doc =Document()
config = doc.createElement('config')
doc.appendChild(config)
LoginInfo = doc.createElement('LoginInfo')
config.appendChild(LoginInfo)
ServiceName = doc.createElement('ServiceName')
LoginInfo.appendChild(ServiceName)
ServiceName_text = doc.createTextNode('104')
ServiceName.appendChild(ServiceName_text)
ServiceIP = doc.createElement('ServiceIP')
LoginInfo.appendChild(ServiceIP)
ServiceIP_text = doc.createTextNode('192.168.37.104:8886')
ServiceIP.appendChild(ServiceIP_text)
ISSSL = doc.createElement('ISSSL')
LoginInfo.appendChild(ISSSL)
ISSSL_text = doc.createTextNode('N')
ISSSL.appendChild(ISSSL_text)
EChecked = doc.createElement('EChecked')
LoginInfo.appendChild(EChecked)
EChecked_text = doc.createTextNode('Y')
EChecked.appendChild(EChecked_text)
UserNo = doc.createElement('UserNo')
LoginInfo.appendChild(UserNo)
UserNo_text = doc.createTextNode('ADMIN')
UserNo.appendChild(UserNo_text)
Passwd = doc.createElement('Passwd')
LoginInfo.appendChild(Passwd)
Passwd_text = doc.createTextNode('nx9TmpOReOkzt/Eb1jYlOw==')
Passwd.appendChild(Passwd_text)
SystemRent = doc.createElement('SystemRent')
config.appendChild(SystemRent)
Skin = doc.createElement('Skin')
SystemRent.appendChild(Skin)
Skin_text = doc.createTextNode('\n\t\t')
Skin.appendChild(Skin_text)
ShowHelpFrom = doc.createElement('ShowHelpFrom')
SystemRent.appendChild(ShowHelpFrom)
ShowHelpFrom_text = doc.createTextNode('Hidden')
ShowHelpFrom.appendChild(ShowHelpFrom_text)
ImportExportCOMBINESUBMIT = doc.createElement('ImportExportCOMBINESUBMIT')
config.appendChild(ImportExportCOMBINESUBMIT)
COMBINESUBMIT = doc.createElement('COMBINESUBMIT')
ImportExportCOMBINESUBMIT.appendChild(COMBINESUBMIT)
COMBINESUBMIT_text = doc.createTextNode('C:\\Users\\zhaoning\\Desktop\\')
COMBINESUBMIT.appendChild(COMBINESUBMIT_text)


f = open('Local.xml','w')
doc.writexml(f,newl = '\n', addindent = '\t',encoding='utf-8')
f.close()
app = Application().start(path_dir_finally+'\\'+mystr[0]+'\\'+mystr[0]+'\\'+"iTapManage.exe")