from functools import *
from itertools import *
import re

ls = [int(l) for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

t = 556543474
for i in range(len(ls)):
    x = 0
    while sum(ls[i:i+x]) < t:
        x += 1
    if sum(ls[i:i+x]) == t:
        print(min(ls[i:i+x])+max(ls[i:i+x]))
