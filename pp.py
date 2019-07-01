#!usr/bin/python

def pp(l):
    c = len(l)

    for i in range(c-1):
        for j in range(c-1-i):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
    print(l)
    return l

if __name__ == '__main__':
    pp([1,5,3,23,23,23])
