ls = [[c == '#' for c in l] for l in iter(input,'')]

def f(X,Y):
    i = 0
    n = 0
    for r in ls[Y::Y]:
        i += X
        n += r[i%len(r)]
    return n

print(f(1,1)*f(3,1)*f(5,1)*f(7,1)*f(1,2))
