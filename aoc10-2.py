from functools import *
from itertools import *
import re

ls = [int(l) for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

ls.sort()

@lru_cache(maxsize=None)
def f(x):
    if x == ls[-1]:
        return 1
    n = 0
    for y in (1,2,3):
        if x+y in ls:
            n += f(x+y)
    return n

print(f(0))
