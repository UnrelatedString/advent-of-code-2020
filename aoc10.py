from functools import *
from itertools import *
import re

ls = [int(l) for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

ls.sort()

##def f(x, os, ts):
##    rs = set()
##    if x+1 in ls:

x = 0
os = 0
ts = 0
for y in ls:
    if y-x==1:
        os += 1
    elif y-x==3:
        ts += 1
    elif y-x>3:
        print('wtf')
    x = y

ts += 1
print(os*ts)
