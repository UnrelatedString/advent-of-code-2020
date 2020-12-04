ls = [l for l in iter(input,'-1')]


fs = "byr iyr eyr hgt hcl ecl pid".split()
n = 0

FS = set()
for l in ls:
    if l == '':
        n += FS >= set(fs)
        FS = set()
    for f in l.split():
        k,v = f.split(':')
        succ = False
        if k == 'byr':
            succ = 1920 <= int(v) <= 2002
        elif k == 'iyr':
            succ = 2010 <= int(v) <= 2020
        elif k == 'eyr':
            succ = 2020 <= int(v) <= 2030
        elif k == 'hgt':
            if v[-2:] == 'cm':
                succ = 150 <= int(v[:-2]) <= 193
            elif v[-2:] == 'in':
                succ = 59 <= int(v[:-2]) <= 76
        elif k == 'ecl':
            succ = v in "amb blu brn gry grn hzl oth".split()
        elif k == 'hcl':
            succ = v[0] == '#' and len(v) == 7 and all(v[i] in '0123456789abcdef' for i in range(1,7))
        elif k == 'pid':
            succ = len(v) == 9 and all(v[i] in '0123456789' for i in range(9))
        if succ: FS.add(k)

print(n)
