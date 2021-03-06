from functools import *
from itertools import *
from math import e, radians
import re

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

p, o = 0, 1

for l in ls:
    i, n = l[0], l[1:]
    for _ in range(int(n)):
        if i == 'E':
            p += 1
        elif i == 'S':
            p += -1j
        elif i == 'W':
            p += -1
        elif i == 'N':
            p += 1j
        elif i == 'F':
            p += o
    if i == 'L':
        o *= e**(1j*radians(int(n)))
    elif i == 'R':
        o *= e**(-1j*radians(int(n)))

print(abs(p.real)+abs(p.imag))
        
