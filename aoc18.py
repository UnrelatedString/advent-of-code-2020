from itertools import *
from functools import *
import re

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

def e(ts):
    s = [lambda x:x]
    for t in ts:
        if re.match(r'\d+',t):
            s[-1] = s[-1](int(t))
        elif t == '(':
            s.append(lambda x:x)
        elif t == ')':
            v = s.pop()
            s[-1] = s[-1](v)
        else:
            v = s[-1]
            s[-1] = { '+': v.__add__,
                      '-': v.__sub__,
                      '*': v.__mul__
                }[t]
    return s[0]

r = 0
for l in ls:
    toks = [*filter(None,re.split(r'([()])|\s',l))]
    r += e(toks)

print(r)
