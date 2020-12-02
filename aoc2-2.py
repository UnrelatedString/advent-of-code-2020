ls = [l.split() for l in iter(input,'')]

n = 0
for r, c, p in ls:
    r = [int(x) for x in r.split('-')]
    c = c[0]
    try:
        n += (p[r[0]-1] == c) ^ (p[r[1]-1] == c)
    except: pass

print(n)
