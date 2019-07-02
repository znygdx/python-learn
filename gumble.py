#!usr/bin/python

from random import randint,randrange,sample
def set_ball():
    '''构造生成器'''
    st = [x for x in range(1,34)]

    '''随机挑6个数'''
    c = sample(st,6)


    '''选蓝球'''
    c.append(randint(1,16))
    print(c)
    return c


if __name__ == '__main__':
    n = int(input("来几注："))


    for _ in range(n):
        set_ball()

