#！/usr/bin/python
import sys



a = int(input("请输入一个数字："))
if a == 1:
    print("%d不是质数" % a)
elif a > 1:
    for i in range(2,a):
        if a % i == 0:
            print('%d不是质数' % a)
            break
    else:
      print('%d是质数' % a)
else:
            print('%d不是质数' % a)
#