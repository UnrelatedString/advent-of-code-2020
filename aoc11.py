from functools import *
from itertools import *
import re

ls = [[*l] for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

ss = []
s = [r[:] for r in ls]
def get0(x,y,l):
    if y < 0 or y >= len(l) or x < 0 or x >= len(l[y]):
        return False
    else:
        return l[y][x]
def mn(x,y,l):
    return sum(get0(x+X,y+Y,l)=='#' for X in [-1,0,1] for Y in [-1,0,1])
while s not in ss:
    ss.append(s)
    n = [r[:] for r in s]
    for y, r in enumerate(s):
        for x, c in enumerate(r):
            if c == 'L':
                n[y][x] = 'L#'[mn(x,y,s)==0]
            elif c == '#':
                n[y][x] = 'L#'[mn(x,y,s)<5] #inclusive
    s = n

print(sum(r.count('#') for r in s))
