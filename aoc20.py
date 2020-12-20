from itertools import *
from functools import *
import re

ls = [l for l in iter(input,'e')]

lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

ts = {}
for lg in lgs:
    lg = lg.split('\n')
    ts[int(re.match(r'Tile (\d+):',lg[0]).groups()[0])] = (
        lg[1],
        ''.join(l[-1] for l in lg[1:]),
        lg[-1][::-1],
        ''.join(l[0] for l in lg[:0:-1]))

adjs = {}
for t in ts:
##    adjs[t] = tuple(tuple((T,(ts[T].index(f)-i-2)%4)
##                          for T in ts if f in ts[T] and T is not t)
##                    for i,f in enumerate(ts[t]))
    a = []
    for f in ts[t]:
        a.append([])
        for T in ts:
            if T is t: continue
            for i, F in enumerate(ts[T]):
                if f == F:
                    a[-1].append((T,i))
                if f[::-1] == F:
                    a[-1].append((T,i+4))
    adjs[t] = tuple(map(tuple,a))

p = 1
for t in ts:
    if adjs[t].count(()) == 2:
        print(t)
        p *= t

print(p)
