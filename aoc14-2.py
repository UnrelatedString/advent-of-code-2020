from functools import *
from itertools import *
import re

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

mem = {}
mask = []
for l in ls:
    if l.startswith('mask = '):
        m = l[7:]
        mask = int(m.replace('X','0'),2)
        masks = [m.replace('1','0')]
        for _ in range(m.count('X')):
            masks = chain.from_iterable(
                (s.replace('X','0',1),s.replace('X','1',1)) for s in masks)
            #masks = [*masks]
        masks = [*map((lambda x: int(x, 2)), masks)]
    else:
        a, v = map(int,re.match(r'mem\[(\d+)\] = (\d+)', l).groups())
        a |= mask
        for m in masks:
            mem[a^m] = v
            

print(sum(mem.values()))
