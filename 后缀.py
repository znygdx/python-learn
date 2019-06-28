#!/usr/bin/python
import os
import time
import math
import random
def get_suffix(filename):
    l = filename.rfind('.')
    d = list(filename)
    c = len(d)
    s = ''
    for i in range(l+1,c):
        s += d[i]
    print(s)

if __name__ == '__main__':
    get_suffix('abc.txt')




