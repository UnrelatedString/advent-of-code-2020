from itertools import *
from functools import *
import re
from copy import deepcopy
import numpy as np

cs = [*map(int,input())] + [*range(10,1000001)]
ps = dict(zip(cs,cs[1:]+cs[0:1]))
v = cs[0]

for _ in range(10000000):
    ns = []
    n = ps[v]
    for _ in range(3):
        ns.append(n)
        n = ps[n]
    d = v
    while d in ns or d == v:
        d -= 1
        d = d or 1000000
    ps[ns[2]] = ps[d]
    ps[d] = ns[0]
    ps[v] = n
    v = n

print(ps[1]*ps[ps[1]])
