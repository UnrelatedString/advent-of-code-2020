from functools import *
from re import split, match

ls = [l for l in iter(input,'')]

cs = {}
for l in ls:
    h, t = l.split(' bags contain ')
    bs = t.split(', ')
    for b in bs:
        b = match(r'\d (.+) bag',b)
        if not b:
            continue
        b = b.groups()[0]
        if b in cs:
            cs[b].add(h)
        else:
            cs[b] = {h}

def growg(g, gs):
    if g in cs:
        for c in cs[g]:
            if c not in gs:
                gs.add(c)
                growg(c, gs)

gs = set()
growg('shiny gold',gs)
print(len(gs))
