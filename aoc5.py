ls = [l for l in iter(input,'')]

m = 0

for l in ls:
    m = max(m,int(l.replace('F','0').replace('B','1').replace('R','1').replace('L','0'),base=2))

print(m)
