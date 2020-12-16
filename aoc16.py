from functools import *
from itertools import *
import re

fs = [l for l in iter(input,'')]

input()
mt = input()

input(); input()
ts = [list(map(int,l.split(','))) for l in iter(input,'')]

rs = []
for f in fs:
    a,b,x,y = map(int,re.match(r'.+: (\d+)-(\d+) or (\d+)-(\d+)', f).groups()
)
    rs.append([*range(a,b+1)])
    rs.append([*range(x,y+1)])

s = 0
for t in ts:
    for n in t:
        if all(n not in r for r in rs):
            s += n

print(s)
