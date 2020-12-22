from itertools import *
from functools import *
import re
from copy import deepcopy

ls = [l for l in iter(input,'e')]

lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

ds = [[*map(int,d.split('\n')[:0:-1])] for d in lgs]

@lru_cache(maxsize=None)
def combat(deckst):
    decks = [*map(list,deckst)]
    seen = set()
    while all(decks):
        state = tuple(map(tuple,decks))
        if state in seen:
            return True, decks[0]
        seen.add(state)
        a,b = map(list.pop,decks)
        if len(decks[0]) >= a and len(decks[1]) >= b:
            #print('ee')
            p1w, _ = combat((tuple(decks[0][::-1][:a][::-1]),tuple(decks[1][::-1][:b][::-1])))
        else:
            p1w = a > b
        if p1w:
            decks[0].insert(0,a)
            decks[0].insert(0,b)
        else:
            decks[1].insert(0,b)
            decks[1].insert(0,a)
        #print(decks)
    return bool(decks[0]), [*chain(*decks)]

s = 0
for i,v in enumerate(combat(tuple(map(tuple,ds)))[1]):
    s += (i+1)*v
print(s)
