from functools import *
from itertools import *
import re

ls = [int(l) for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

xs = ls[:25]

for y in ls[25:]:
    for x in xs:
        if y-x in xs and y-x != x:
            break
    else:
        print(y)
