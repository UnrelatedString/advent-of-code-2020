from itertools import *
from functools import *
import re
from copy import deepcopy

ls = [l for l in iter(input,'e')]

lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

decks = [[*map(int,d.split('\n')[:0:-1])] for d in lgs]

while all(decks):
    a,b = map(list.pop,decks)
    if a > b:
        decks[0].insert(0,a)
        decks[0].insert(0,b)
    else:
        decks[1].insert(0,b)
        decks[1].insert(0,a)

s = 0
for i,v in enumerate(chain(*decks)):
    s += (i+1)*v
print(s)
