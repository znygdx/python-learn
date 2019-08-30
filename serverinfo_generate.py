import os
import hashlib
import codecs
import re
import binascii
from ctypes import *

def getmd5(file):
    if(not os.path.exists(file)): return ''
    fd = open(file, 'rb')
    md5obj = hashlib.md5()
    while True:
        info = fd.read(8096)
        if not info: break
        md5obj.update(info)
    hash_code = md5obj.hexdigest()
    fd.close()
    md5 = str(hash_code).lower()
    return md5

def get_vsinzip(file):
    with codecs.open (file,encoding='utf-8-sig',errors='ignore') as f:
        first_line = str(f.readlines()[0])
        vs_intxt = ((first_line.split('(')[0]))
        return (vs_intxt)

parent_dir = input("请输入你的父目录:")
L = os.listdir(parent_dir)
L = L[:-2]
os.chdir(parent_dir)
total_version = []
total_version_finally = []
total_file_ingate = []
total_file_ingatecfg = []
#取出来每个网关的版本号，生成列表
for i in range(0,len(L)):
    path_gatedir = os.path.join(parent_dir,L[i])


#对bin目录下的每个子目录处理，获取其中version.txt里边的版本号(total_version_finally)
    path_version = path_gatedir + '\\'+'Version.txt'
   # print(path_version)
    version_num = get_vsinzip(path_version)
    total_version.append(version_num)
    #print(total_version)
for j in total_version:
   # version_num1 = re.compile(r'\d\.\d.\d.\d').search(j).group()
    version_num1 = re.search(r'\d\.\d.\d*.\d',j).group()
    total_version_finally.append(version_num1)
#print(len(total_version_finally))
#取出来每个网关目录的主程序(total_file_ingate)和配置文件(total_file_ingatecfgnew)，分别生成列表
for i in range(0,len(L)):
    path_gatedir = os.path.join(parent_dir,L[i])
    os.chdir(path_gatedir)
    file_ingate = os.listdir(path_gatedir)
    new_file_ingate = list(filter(lambda x:re.match('itap.*',x) != None,file_ingate))
    new_file_ingate2 = list(filter(lambda x:re.match('itap.*',x) == None,file_ingate))
    new_file_ingate3 = ','.join(new_file_ingate2)
    new_file_ingate1= ','.join(new_file_ingate)
    total_file_ingate.append(new_file_ingate1)
    total_file_ingatecfg.append(new_file_ingate3)
total_file_ingatecfgnew1 = [i.split(',') for i in total_file_ingatecfg]
print(total_file_ingatecfgnew1)
total_file_ingatecfgnew2 =[]
for i in range(0,len(total_file_ingatecfgnew1)):
    total_file_ingatecfgnew2 += total_file_ingatecfgnew1[i]
total_file_ingatecfgnew3 = list(set(total_file_ingatecfgnew2))
total_file_ingatecfgnew = list(filter(lambda x:re.search('.xml|.txt|.py',x)==None,total_file_ingatecfgnew3))


#获得主服务和版本号字典
dic_service_version = dict(zip(total_file_ingate,total_version_finally))


#获得各个服务的md5
total_dir_file=[]
for root,dirs,files in os.walk(parent_dir):
    for file in files:
        total_dir_file.append(os.path.join(root,file))
total_dir_files =list(filter(lambda x:re.search('.xml|.txt|.py|.sql|.sh',x)==None,total_dir_file))
total_dir_filesN=[i.split('\\')[-1] for i in total_dir_files]
total_md5_dir = [getmd5(i) for i in total_dir_files]
dic_md5=dict(zip(total_dir_filesN,total_md5_dir))

#获取最终要写入的文件流
for key in dic_service_version.keys():
    if key in dic_md5.keys():
        dic_md5[key]=dic_service_version[key]+'@'+dic_md5[key]
list_key = list(dic_md5)
list_value=list(dic_md5.values())
total_final=[]
for i in range(0,len(list_key)):
    list_final = list_key[i]+'@'+list_value[i]
    total_final.append(list_final)

for i in range(0,len(total_final)):
    serv_list=list(total_final[i])
    if serv_list.count('@')==1:
        serv_list.insert(serv_list.index('@'),'@')
        serv_str = ''.join(serv_list)
        total_final[i]=serv_str
print(total_final)

#对packageversion
total_final.append('PackageVersion@9.3.1@')
#对脚本md5处理
total_final.append('TapDataBaseAfter@9.3.1@c17982222499b50944734538ef1b382e')
#对动态库版本处理


class TServerInfoVersion(Structure):
    _pack_  = 1
    _fields_  =  [
        ('ServerName',       c_char * 51),
        ('ServerVersion',    c_char * 51),
        ('ServerMD5',        c_char * 51)
    ]

total_bytes=[]
for i in total_final:
    a=TServerInfoVersion()
    a.ServerName = i.split('@',1)[0].encode('utf-8')
    a.ServerVersion = i.split('@',2)[1].encode('utf-8')
    a.ServerMD5 =i.split('@',2)[2].encode('utf-8')
    strinfo=binascii.hexlify(a).upper()
    total_bytes.append(strinfo)


with open('d:\\2019\\serverinfo','wb') as f:
    for i in total_bytes:
        f.write(i)
        f.write(b'\r\n')







