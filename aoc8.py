from functools import *
import re

ls = [(*l.split(),False) for l in iter(input,'')]

acc = 0
i = 0
while not ls[i][2]:
    op, n, f = ls[i]
    ls[i] = (op, n, True)
    if op == 'jmp':
        i += int(n)
        continue
    elif op == 'acc':
        acc += int(n)
    i += 1
    i %= len(ls)

print(acc)
