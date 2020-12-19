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
        return m[0] == r[1] and m[1:]
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
    c += match(m,'0') == ''
print(c)

