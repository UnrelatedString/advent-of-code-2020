from functools import *
from re import split, match

ls = [l for l in iter(input,'')]

cs = {}
for l in ls:
    h, t = l.split(' bags contain ')
    bs = t.split(', ')
    cs[h] = set()
    for b in bs:
        b = match(r'(\d) (.+) bag',b)
        if not b:
            continue
        n, b = b.groups()
        cs[h].add((int(n),b))

def f(g):
    if g not in cs:
        return 0
    else:
        s = 0
        for n,b in cs[g]:
            s += n
            s += n * f(b)
        return s

print(f('shiny gold'))
