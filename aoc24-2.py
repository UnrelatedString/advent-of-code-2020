from itertools import *
from functools import *
import re
from copy import deepcopy
from math import e, pi

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

ds = (1+1j,2,1-1j,-1-1j,-2,-1+1j)
ts = []
for l in ls:
    t = 0
    while l:
        d = l[0]
        if d in 'ns':
            d = l[0:2]
        l = l[len(d):]
        t += ds['ne e se sw w nw'.split().index(d)]
    ts.append(t)

mx = min(t.real for t in ts)
my = min(t.imag for t in ts)

def flip(t,g):
    while t.imag >= len(g):
        g.append([])
    while t.real >= len(g[int(t.imag)]):
        g[int(t.imag)].append(False)
    g[int(t.imag)][int(t.real)] ^= True

def hggm(X,Y,g):
    return 0 <= Y < len(g) and 0 <= X < len(g[Y]) and g[Y][X]

def mns(x,y,g):
    s = 0
    for d in ds:
        X = x+int(d.real)
        Y = y+int(d.imag)
        s += hggm(X,Y,g)
    return s

g = [[]]
for t in ts:
    flip(t-complex(mx,my),g)
    
#print(sum(sum(r) for r in g))
for _ in range(100):
    ng = [[]]
    w = max(len(r) for r in g)
    for y in range(len(g)+2):
        for x in range(w+2):
            if hggm(x-1,y-1,g):
                s = mns(x-1,y-1,g)
                flip(complex(x,y),ng)
                if s == 0 or s > 2:
                    flip(complex(x,y),ng)
            else:
                if mns(x-1,y-1,g) == 2:
                    flip(complex(x,y),ng)
    g = ng

print(sum(sum(r) for r in g))
