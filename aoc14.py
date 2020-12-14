from functools import *
from itertools import *
import re

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

mem = {}
mask = None
for l in ls:
    if l.startswith('mask = '):
        m = l[7:]
        mask = (int(m.replace('X','0'),2),int(m.replace('X','1'),2))
    else:
        a, v = map(int,re.match(r'mem\[(\d+)\] = (\d+)', l).groups())
        mem[a] = (v | mask[0]) & mask[1]

print(sum(mem.values()))
