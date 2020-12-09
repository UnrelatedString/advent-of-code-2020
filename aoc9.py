from functools import *
from itertools import *
import re

ls = [int(l) for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

for i in range(25,len(ls)):
    l = ls[i]
    for x in ls[i-25:i]:
        if l-x in ls[i-25:i] and l-x != x:
            break
    else:
        print(l)
