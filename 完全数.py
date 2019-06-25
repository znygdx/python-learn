#!/usr/bin/python
import math
a = int(input("请输入数字:"))
x = 0
for i in range(a-1,0,-1):
    while a % i ==0:
        x+=i
        break
if x == a:
    print("%d是完全数" % x)
else:
    print("%d不是完全数" % x)