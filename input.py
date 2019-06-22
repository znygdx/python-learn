#!/usr/bin/python
#coding=utf-8

import sys
import os

#python3只有input,由于input返回是string，所以需要用int转
try:
    lin1=int(input('请输入第一条边：'))
    lin2=int(input('请输入第二条边：'))
    lin3=int(input('请输入第三条边：'))
# {}是占位符，format函数对数据格式化
except Exception:
    print ("不支持小数")
else:
    print('周长是{}'.format(lin1+lin2+lin3))