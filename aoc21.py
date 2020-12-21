from itertools import *
from functools import *
import re
from copy import deepcopy

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

alcs = {}
cs = {}
for l in ls:
    #ings, _, als = re.match(r'(.+) (\(contains (.+)\))?',l).groups()
    ings, als, *_ = *l.replace(')','').split(' (contains '), None
    #print(ings,als)
    for i in ings.split():
        cs[i] = cs.get(i,0) + 1
    if als:
        for a in als.split(', '):
            if a not in alcs:
                alcs[a] = {*ings.split()}
            alcs[a] &= {*ings.split()}

s = 0
for i,c in cs.items():
    if i not in chain(*alcs.values()):
        s += c

print(s)
