#!/usr/bin/python
import math
count = 0
while 1:
    a = int(input("请输入："))
    b = len(str(a))
    count +=1
    c = a // 100
    d = a % 100 // 10
    e = a % 10
    f = math.pow(a // 100,3)
    g = math.pow(a % 100 // 10,3)
    h = math.pow(a % 10,3)
    if f + g + h == c + d + e:
        print("是水仙花")
    else:
        print("bus")



