#！/usr/bin/python
import datetime
def time_d(y,m,d):
    d1 = datetime.date(2019,7,2)
    d2 = datetime.date(2019,m,d)
    s = d2 -d1
    l = d - d //7 * 2
    if l % 3 ==0:
        print("康剑")
    elif l % 3 == 1:
        print("孙志中")
    else:
        print("曹志明")
    return s

if __name__ == '__main__':
    time_d(2019,7,8)