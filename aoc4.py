ls = [l for l in iter(input,'-1')]


fs = "byr iyr eyr hgt hcl ecl pid".split()
n = 0

FS = set()
for l in ls:
    if l == '':
        n += FS >= set(fs)
        FS = set()
    for f in l.split():
        k = f.split(':')[0]
        FS.add(k)

print(n)
