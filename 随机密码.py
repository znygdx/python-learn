import math
import random
def generat(i):
    v = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    c = len(v)-1
    s = ''
    for _ in range((i)):
        l = random.randint(0,c)

        s += v[l]
    print(s)


if __name__ == '__main__':
    generat(5)