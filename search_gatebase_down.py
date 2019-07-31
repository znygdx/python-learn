#!/usr/bin/python
# coding=utf-8
import os
import re
from ftplib import FTP
import functools
import zipfile
import shutil

#��txt�ļ�ת�����ֵ�
def generate_dic(file_path):
    with open(file_path,'r',encoding ='utf-8' ) as f:
        dic = {}
        for i in f:
            line = i.strip('\n').split(' ')
            while '' in line:
                line.remove('')
            (key,value) = line
            dic[key] = value
    return(dic)

#�Ƚ������ֵ���key��ͬvalue��ͬ��ֵ������ӡ����
def compare_two_dict(dict1, dict2, key_list):
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    keys = []
    values = []
    dic1 = globals()
    for key in key_list:
        if key in keys1 and key in keys2:
           if dict1[key] != dict2[key]:
                result = globals()
                result = dict2[key]
                keys.append(key)
                values.append(result)
                dic1 = dict(zip(keys,values))
    return(dic1)

def compare_version(x,y):
    va = x.split('_')[1]
    vb = y.split('_')[1]
    la = [int(i) for i in va.split('.')]
    lb = [int(i) for i in vb.split('.')]
    if la[0] > lb[0]:
        return 1
    elif la[0] < lb[0]:
        return -1
    else:
        if la[1] > lb[1]:
            return 1
        elif la[1] < lb[1]:
            return -1
        else:
            return 0


s= generate_dic('d:/Version.txt')
t= generate_dic('d:/fabu/Version.txt')
new_list = []
for k in t:
    new_list.append(k)
dic1 = compare_two_dict(s,t,new_list)


def download(f,localpath):
    bufsize=1024
    file_handle=open(localpath,"wb")
    f.retrbinary("RETR " + localpath.split('\\')[1],file_handle.write,bufsize)
    file_handle.close()
    print('�������')

#file��·��+�ļ����֣�����'d:\\EsGateway_CQG_862\Version.txt'��
def get_vsinzip(file):
    with open (file,encoding='utf-8-sig') as f:
        first_line = str(f.readlines()[0])
        vs_intxt = ((first_line.split('(')[0]))
        return (vs_intxt)

f = FTP()
f.encoding = 'utf-8'
f.connect('10.12.12.9',port=8801)
f.login('chengyu','chengyu0501')
f.cwd('����/��������/������')
z = f.nlst()
#��������Ŀ¼���ҳ�ʱ���ǰ���������Ŀ¼
ls1 = sorted(z, key=functools.cmp_to_key(compare_version))
newGate_subdir = ls1[-5:]
print(newGate_subdir)

#�±ߵ�dic1���ϱ�compare��������ֵ䣬��dic1����ȡ��key
s = ','.join(i for i in dic1)
print(dic1)
s1 = s.split(',')
s2 = [i.split('itap')[1].split('trade')[0] for i in s1]
s2.remove('')
#s3��Ҫƥ�����������
s3 = ','.join(s2).split(',')
print(s3)

#��s3��dic1����������Ҫ�ҵ����أ��汾���ֵ�
total_key = []
total_value = []
for i in dic1.keys():
    total_key.append(i)
for j in dic1.values():
    total_value.append(j)

total_key1 = []
total_value1 = []

for i in total_key:
    for j in s3:
        if j in i:
            total_key1.append(i)
#print(total_key1)
for key in total_key1:
    if key in dic1.keys():
        total_value1.append(dic1[key])
new_dicgate = dict(zip(total_key1,total_value1))
print(new_dicgate)



s4 = ','.join(s3).upper().split(',')
for newGateway_dir in newGate_subdir:
    print(newGateway_dir)
    for gate_to_search in s4:
        print(gate_to_search)
        if gate_to_search in newGateway_dir:

            f.cwd(newGateway_dir+'/Gateway')
            gateway_sub = f.nlst()
            print(gateway_sub)
            for gate_zip in gateway_sub:
                print(gate_zip)
                if gate_to_search in gate_zip:
                    print('ok')
                    download(f,'d:\\'+gate_zip)
                    myzip = zipfile.ZipFile('d:\\' + gate_zip)
                    print(myzip.filename)
                    mystr = myzip.filename.split('\\')[-1].split('.')
                    # mystr = myzip.filename.split('.')
                    gate_no_zip = mystr[0]
                    print(mystr[0])
                    # mystr1������Ϊ���ܹ���ѹ���ļ���
                    mystr1 = myzip.filename.split('.')
                    print(mystr1)
                    myzip.extractall(mystr1[0])
                    file = 'd:\\' + gate_no_zip + '\\' + gate_no_zip + '\Version.txt'
                    vs_down = get_vsinzip(file)
                    print(vs_down)


                    gate_to_search1 = gate_to_search.lower()
                    gate_to_search2 = 'itap' + gate_to_search1 + 'trade'
                    print(gate_to_search2)
                    if gate_to_search2 in new_dicgate.keys():
                        value1 = new_dicgate[gate_to_search2]
                        value2 = value1.split('V')[1]
                        print(value2)
                        if  vs_down == value2:
                #shutilģ���ƶ���ָ���ļ���
                            shutil.move(mystr1[0],'d:\\fabu')
                            print('���ҵ������ƶ����ļ���d:\\fabu\\%s '% mystr[0] )
                        else:
                            print('�汾����ȣ�δ�ҵ�')

                    f.cwd('..')
                    f.cwd('..')
                    break



                    #
                    # file = 'd:\\'+gate_no_zip+'\\'+gate_no_zip+'\Version.txt'
                   # v_wind = get_vsinzip(file)




                #f.cwd('..')
                else:
                    print('����')
        else:
            print('not in')



