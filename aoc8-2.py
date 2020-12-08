from functools import *
import re

Ls = [(*l.split(),False) for l in iter(input,'')]

def e(ls,s):
    acc = 0
    i = 0
    while not ls[i][2]:
        op, n, f = ls[i]
        ls[i] = (op, n, True)
        if op == 'acc':
            acc += int(n)
        elif (op == 'jmp') ^ (i == s):
            i += int(n) - 1
        i += 1
        if i >= len(ls):
            return acc
    return -9999999

print(max(e(Ls[:],s) for s in range(len(Ls))))
