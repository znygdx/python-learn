#!/usr/bin/python
import random
a = random.randint(1,6)
b = random.randint(1,6)
d = a + b
print(d)
if a + b == 11 or a + b == 7:
    print("u win1")
elif a + b == 2 or a + b == 3 or a + b ==12:
    print("u lose2")
else:
    count = 0
    while 1:
        count += 1
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = a + b
        print(c)
        if d == c:
            print("u win3")
            break
        elif d == 7:
            print("u lose4")
            break
