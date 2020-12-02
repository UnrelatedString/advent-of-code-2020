ls = [l.split() for l in iter(input,'')]

n = 0
for r, c, p in ls:
    r = [int(x) for x in r.split('-')]
    c = c[0]
    if p.count(c) >= r[0] and p.count(c) <= r[1]:
        n += 1
