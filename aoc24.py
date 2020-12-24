from itertools import *
from functools import *
import re
from copy import deepcopy
from math import e, pi

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

ts = set()
for l in ls:
    t = 0
    while l:
        d = l[0]
        if d in 'ns':
            d = l[0:2]
        l = l[len(d):]
        t += e**(1j*pi*'ne e se sw w nw'.split().index(d)/3)
    t = complex(round(t.real,5),round(t.imag,5))
    ts ^= {t}

print(len(ts))
