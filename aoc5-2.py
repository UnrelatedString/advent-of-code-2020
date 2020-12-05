ls = [l for l in iter(input,'')]

ss = []

for l in ls:
    ss.append(int(l.replace('F','0').replace('B','1').replace('R','1').replace('L','0'),base=2))

for s in range(9000):
    if s+1 in ss and s-1 in ss and s not in ss:
        print(s)
