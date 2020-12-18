from itertools import *
from functools import *
import re

ls = [l for l in iter(input,'')]

#lgs = '\n'.join(l).rstrip('\n').split('\n\n')

def e(ts):
    q = []
    os = []
    for t in ts:
        if re.match(r'\d+',t):
            q.append(int(t))
        elif t == '(':
            os.append(t)
        elif t == ')':
            while os[-1] != '(':
                q.append(os.pop())
            os.pop()
        elif t == '*':
            while os and os[-1] == '+':
                q.append(os.pop())
            os.append(t)
        elif t == '+':
            os.append('+')
    while os:
        q.append(os.pop())
    s = []
    for t in q:
        if t == '+':
            s.append(s.pop()+s.pop())
        elif t == '*':
            s.append(s.pop()*s.pop())
        else:
            s.append(t)
    return s[0]
            

r = 0
for l in ls:
    toks = [*filter(None,re.split(r'([()])|\s',l))]
    r += e(toks)

print(r)
