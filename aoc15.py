from functools import *
from itertools import *
import re

ns = eval(f'[{input()}]')

for _ in range(len(ns),2020):
    n = ns[-1]
    i = len(ns)
    if n in ns[:-1]:
        for j in range(2,i+1):
            if ns[-j] == n:
                ns.append(j-1)
                break
    else:
        ns.append(0)

print(ns[2019])
