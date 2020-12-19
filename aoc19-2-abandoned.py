from itertools import *
from functools import *
import re

rls = [l for l in iter(input,'')]

ms = [*iter(input,'')]

rs = {}
for l in rls:
    n, r = l.split(': ')
    rs[n] = [a.split(' ') for a in r.split(' | ')]

##rs['8'] = [['42'],['42','8']]
##rs['11'] = [['42','31'],['42','11','31']]
##
##def match(m,r):
##    if type(r) is list:
##        if r:
##            for M in match(m,r[0]):
##                if M != False:
##                    yield from match(M,r[1:])
##        else:
##            #print(m)
##            yield m
##    elif re.match(r'"."',r):
##        yield m and m[0] == r[1] and m[1:]        
##    else:
##        for a in rs[r]:
##            yield from match(m,a)
##
##c = 0
##for m in ms:
##    if any(M == '' for M in match(m,'0')):
##        print(m)
##    c += any(M == '' for M in match(m,'0'))
##print(c)

def unmatch(r):
    if re.match(r'"."',r):
        yield r[1]
    else:
        for a in rs[r]:
            for p in product(*(unmatch(b) for b in a)):
                #print(p)
                yield ''.join(p)

ft, to = {*unmatch('42')}, {*unmatch('31')}

c = 0

for m in ms:
    n = 0
    Ms = []
    while True:
        for f in ft:
            for 
