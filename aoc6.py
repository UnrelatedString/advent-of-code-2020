ls = '\n'.join([l for l in iter(input,'-1')])

gs = ls.split('\n\n')

n = 0
for g in gs:
    s = set()
    for p in g.split('\n'):
        s |= set(p)
    n += len(s)
print(n)
