from functools import *
from itertools import *
import re

fs = [l for l in iter(input,'')]

input()
mt = input().split(',')

input(); input()
ts = [list(map(int,l.split(','))) for l in iter(input,'')]

rs = {}
for f in fs:
    a,b,x,y = map(int,re.match(r'.+: (\d+)-(\d+) or (\d+)-(\d+)', f).groups()
)
    w, = re.match(r'(.+):', f).groups()
    rs[w] = {*range(a,b+1),*range(x,y+1)}
##
##ps = set(permutations(rs.keys()))
##for t in ts:
##    ppps = pps.copy()
##    for i, n in enumerate(t):
##        for p in ps:
##            if n not in p[i]:
##                ppps.remove(p)
##                break
##    ps = ppps or ps
##
##print(len(ps))
##perm = ps[0]

##ps = [{*rs.keys()} for _ in mt]
##
##for t in ts:
##    for n, p in zip(t, ps):
##        pp = {k for k in p if n in rs[k]}
##        if pp:
##            if p - pp: print(p-pp,n)
##            p &= pp
##        else:
##            break
##
##
##ps = [*map(list,ps)]
##pps = []
##xr = reduce(int.__mul__, map(len, ps))
##print(xr)
##exit()
##for x in range(xr):
##    pp = []
##    for p in ps:
##        pp.append(p[x%len(p)])
##        x //= len(p)
##    if len(set(pp)) == len(pp):
##        pps.append(pp)
##        print('e')
##
##perm = pps[0]

tr = set.union(*rs.values())
cs = [*map(set,zip(*filter(lambda t: all(n in tr for n in t),ts)))]
ps = [{k for k in rs.keys() if rs[k] >= c} for c in cs]
while max(map(len,ps)) > 1 and min(map(len,ps)) == 1:
    for p in ps:
        if len(p) == 1:
            for P in ps:
                if p is not P:
                    P -= p

print(*map(len,ps))

perm = next(zip(*ps))

ds = [*filter(lambda k:k.startswith('departure'), rs.keys())]
p = 1
for d in ds:
    i = perm.index(d)
    p *= int(mt[i])

print(p)
