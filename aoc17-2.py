from itertools import *
from functools import *
import re

grid = [[[[c == '#' for c in l] for l in iter(input,'')]]]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

def mdget(g,il):
    return reduce((lambda l,i: bool(l) and 0 <= i < len(l) and l[i]),il,g)

def mn(g,il):
    ds = (-1,0,1)
    for os in product(*(ds for _ in il)):
        yield mdget(g,map(sum,zip(os,il)))

def deepzero(g):
    if type(g) is not list:
        return 0
    return [*map(deepzero,g)]

def pad(g):
##    if type(g) is not list:
##        return (g, 0)
##    P = pad(g[0])[1]
##    p = [P]*len(g)
##    return ([p[:],*map(lambda l:pad(l)[0],g),p[:]],p[:])
    if type(g) is not list:
        return g
    hp = [*map(pad,g)]
    p = deepzero(hp[0])
    return [p,*hp,p]

def shape(g):
    if type(g) is list:
        yield len(g)
        yield from shape(g[0])

def deepim(f,dil,il=()):
    if not dil:
        return f(il)
    else:
        return [deepim(f,dil[1:],il+(i,)) for i in range(dil[0])]

def deepsum(g):
    if type(g) is list:
        return sum(map(deepsum,g))
    else:
        return g

def tick(g):
    g = pad(g)
    return deepim((lambda il: #print(sum(mn(grid,il))) or 
                             sum(mn(g,il)) in (4,3)[not mdget(g, il):]
                       ),[*shape(g)])

for _ in range(6):
    #print(deepsum(grid))
    grid = tick(grid)
    #print([*shape(grid)])
    

print(deepsum(grid))
