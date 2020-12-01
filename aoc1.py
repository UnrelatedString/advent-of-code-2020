es = [int(i) for i in iter(input,'')]

for i in range(len(es)):
    for y in es[i+1:]:
        for z in es[i+1:]:
            x = es[i]
            if x+y+z==2020:
                print(x*y*z)
