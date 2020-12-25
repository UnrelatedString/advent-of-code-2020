from itertools import *
from functools import *
import re
from copy import deepcopy

ls = [int(l) for l in iter(input,'')]

#lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

mod = 20201227

xs = set()
for x in count(1):
    if pow(7,x,mod) in ls:
        ls.remove(pow(7,x,mod))
        print(pow(ls.pop(),x,mod))
