ls = '\n'.join([l for l in iter(input,'-1')])

gs = ls.split('\n\n')

n = 0
for g in gs:
    ps = g.split('\n')
    s = None
    for p in ps:
        if s is None:
            s = set(p)
        s &= set(p)
    n += len(s)
print(n)
