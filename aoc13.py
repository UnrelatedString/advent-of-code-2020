from functools import *
from itertools import *
import re

n = int(input())
ids = [int(x) for x in input().split(',') if x != 'x']

x = n
while all(x % i for i in ids):
    x += 1
for i in ids:
    if not x%i:
        print(i*(x-n))
