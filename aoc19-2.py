from itertools import *
from functools import *
import re

rls = [l for l in iter(input,'')]

ms = [*iter(input,'')]

rs = {}
for l in rls:
    n, r = l.split(': ')
    rs[n] = [a.split(' ') for a in r.split(' | ')]

def match(m,r):
    if re.match(r'"."',r):
        return m and m[0] == r[1] and m[1:]
    else:
        for a in rs[r]:
            M = m
            for b in a:
                M = match(M,b)
                if M == False: break
            else:
                return M
        return False

c = 0
for m in ms:
    n = 0
    # wishing I'd updated to 3.8 right about now
    while True:
        M = match(m,'42')
        if M:
            m = M
            n += 1
        else:
            break
    while m and n > 1:
        m = match(m,'31')
        n -= 1
    c += m == ''
print(c)

