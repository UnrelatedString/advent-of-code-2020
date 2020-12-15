from functools import *
from itertools import *
import re

ns = eval(f'[{input()}]')

ts = dict(map(reversed,enumerate(ns[:-1])))

n = ns[-1]
lim = 30000000
for i in range(len(ns)-1,lim-1):
    #print(n,ts)
    a = ts.get(n,i)
    ts[n] = i
    n = i - a

print(n)
