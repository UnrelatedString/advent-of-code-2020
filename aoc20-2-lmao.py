from itertools import *
from functools import *
import re
from copy import deepcopy
from random import getrandbits

glen = 12 #12

ls = [l for l in iter(input,'e')]

lgs = '\n'.join(ls).rstrip('\n').split('\n\n')

while True:
    ts = {}
    cs = {}
    for lg in lgs:
        lg = lg.split('\n')
        t = int(re.match(r'Tile (\d+):',lg[0]).groups()[0])
        ts[t] = (
            lg[1],
            ''.join(l[-1] for l in lg[1:]),
            lg[-1][::-1],
            ''.join(l[0] for l in lg[:0:-1]))
        cs[t] = [l[1:-1] for l in lg[2:-1]]

    adjs = {}
    for t in ts:
        a = []
        for f in ts[t]:
            a.append([])
            for T in ts:
                if T is t: continue
                for i, F in enumerate(ts[T]):
                    if f == F:
                        a[-1].append((T,i,False))
                    if f[::-1] == F:
                        a[-1].append((T,i,True))
        adjs[t] = tuple(map(tuple,a))

    S = None
    for t in ts:
        if adjs[t][0] == adjs[t][3] == ():
            S = t
            break

    def rot(c,x): #cw
        for _ in range(x):
            c = [*zip(*c[::-1])]
        return c

    ##def gen(s, ors):
    ##    try:
    ##        o = 0
    ##        r = False #vertical flip after rotation
    ##        g = [[]]
    ##        while len(g) <= 12:
    ##            g[-1].append((s,o,r))
    ##            if adjs[s][(1-o)%4] and len(g[-1]) < 12:
    ##                (s,f,R), = adjs[s][(1-o)%4]
    ##                o = (3-f)%4
    ##                r ^= R
    ##        ##    elif adjs[s][(3-o)%4] and len(g[-1]) < 12: #!?!?!!?!?!??!?!
    ##        ##        (s,f,R), = adjs[s][(3-o)%4]
    ##        ##        o = (1-f)%4
    ##        ##        r ^= R
    ##            else:
    ##                s,o,r = g[-1][0]
    ##                i = (2-o+(2*r))%4
    ##                if adjs[s][i]:
    ##                    #print(o,r,len(g[-1]))
    ##                    (s,f,R), = adjs[s][i]
    ##        ##            r ^= R
    ##        ##            print(r,R,o,f,len(g[-1]))
    ##        ####            if len(g)%2:
    ##        ####                f += 2
    ##        ####                r ^= 1
    ##        ##            o = (-(2*r)-f)%4#(3-adjs[s].index(())-(2*r))%4#((2*r)-f)%4
    ##        ##            g.append([])
    ##        ####            if len(g) == 12:
    ##        ####                print(adjs[s])
    ##        ####                o -= 1
    ##        ####                r ^= 1
    ##        ##            #print(adjs[s],o,r)
    ##                    #print(len(g[-1]))
    ##                    o, r = ors[len(g)-1]
    ##                    g.append([])
    ##                else:
    ##                    break
    ##        if len(g) == 12 and all(len(l) == 12 for l in g) and len(set(chain(*g))) == 144:
    ##            yield g
    ##    except IndexError as e:
    ##        print(e)
    ##        pass
    ##
    ##g = next(chain.from_iterable(map(lambda ors:gen(S,ors),combinations_with_replacement(product(range(4),range(2)),13))))

    def row(start):
        for x in range(8):
            s = start
            o = x%4
            r = x//4
            g = [(s,o,r)]
            while adjs[s][(1-o)%4]:
                (t,f,R), = adjs[s][(1-o)%4]
                g.append((t,(3-f)%4,r^R))
                s,o,r = g[-1]
            if len(g) == glen:
                yield g
    rows = {}
    for t in ts:
        rs = row(t)
        for r in rs:
            if r[-1][0] != S and (t not in rows or getrandbits(1)):
                rows[t] = r
            

    col = [S]
    for _ in range(glen-1):
        for a in adjs[col[-1]]:
            if a and a[0][0] not in [r[0] for r in rows[S]] and a[0][0] in rows and a[0][0] not in col:
                col.append(a[0][0])
                break

    for i in range(glen-1):
        if rows[col[i]][i+1] not in (f[0] for f in adjs[col[i+1]] if f):
            break
    else:
        print('blessed')
    
    g = []
    seens = set()
    for c in col:
        R = []
        for (t,o,r) in rows[c]:
            seens.add(t)
            s = cs[t]
            s = rot(s,o)
            if r:
                s = s[::-1]
            R.append(s)
        g.extend(map(list,map(chain.from_iterable,zip(*R))))

    # SEA MONSTER TIME

    def remove_monsters(grid):
        inds = (0,1),(1,2),(4,2),(5,1),(6,1),(7,2),(10,2),(11,1),(12,1),(13,2),(16,2),(17,1),(18,0),(18,1),(19,1)
        for y in range(len(grid)-2):
            for x in range(len(grid[0])-18):
                #print('a')
                for X,Y in inds:
                    if grid[y+Y][x+X] != '#':
                        break
                else:
                    #print('boom')
                    for X,Y in inds:
                        grid[y+Y][x+X] = '.'

    def roughness(grid):
        return sum(sum(t == '#' for t in r) for r in grid)

    br = roughness(g)
    for x in range(8):
        o = x%4
        r = x//4
        grid = [*map(list,rot(g,o))]
        if r:
            grid = grid[::-1]
        remove_monsters(grid)
        pr = roughness(grid)
        if pr < 2124 and len(seens) == glen**2:
            print(pr)
        
