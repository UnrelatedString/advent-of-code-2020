from functools import *
from itertools import *
import re
from math import gcd


input()
ids = input().split(',')

##x = 2
##while True:
##    for n, i in enumerate(ids):
##        if i == 'x':
##            continue
##        elif (x+n)%int(i):
##            break
##    else:
##        print(x)
##        break
##    x += 1
##

rs = [(r, int(i)) for r, i in enumerate(ids) if i != 'x']

x = sum(rs[0])
l = rs[0][1]
for r, m in rs[1:]:
    while (x+r)%m:
        x += l
    l = (l*m)//gcd(l,m)
print(x)
