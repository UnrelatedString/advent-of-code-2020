from functools import *
from itertools import *
from math import e, radians
import re

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

p, w = 0, 10+1j

for l in ls:
    i, n = l[0], l[1:]
    for _ in range(int(n)):
        if i == 'E':
            w += 1
        elif i == 'S':
            w += -1j
        elif i == 'W':
            w += -1
        elif i == 'N':
            w += 1j
        elif i == 'F':
            p += w
    if i == 'L':
        w *= e**(1j*radians(int(n)))
    elif i == 'R':
        w *= e**(-1j*radians(int(n)))

print(abs(p.real)+abs(p.imag))
        
