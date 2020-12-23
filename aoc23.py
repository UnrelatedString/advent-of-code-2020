from itertools import *
from functools import *
import re
from copy import deepcopy

cs = [*map(int,input())]

for _ in range(100):
    p = cs[1:4]
    d = cs[0]-1 or 9
    while d in p:
        d -= 1
        d = d or 9
    i = cs.index(d)
    cs = cs[4:i+1]+p+cs[i+1:]+cs[0:1]

print(''.join(map(str,cs)))
