#!/usr/bin/python
import math
a = int(input("����������:"))
x = 0
for i in range(a-1,0,-1):
    while a % i ==0:
        x+=i
        break
if x == a:
    print("%d����ȫ��" % x)
else:
    print("%d������ȫ��" % x)