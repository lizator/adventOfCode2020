

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


res = 0
passport = ""
correct = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for i in range(1001):
    inp = input()
    if inp == "":
        ls = passport.split(" ")
        mapp = {}
        for i in range(len(ls)):
            tmp = ls[i].split(":")
            mapp[tmp[0]] = tmp[1]
        b = True
        for c in correct:
            if not c in mapp.keys():
                b = False

        if b:

            c = False
            if representsInt(mapp['byr']):
                byr = int(mapp['byr'])
                if 1920 <= byr <= 2002:
                    c = True

            if c:
                c = False
                if representsInt(mapp['iyr']):
                    iyr = int(mapp['iyr'])
                    if 2010 <= iyr <= 2020:
                        c = True

            if c:
                c = False
                if representsInt(mapp['eyr']):
                    eyr = int(mapp['eyr'])
                    if 2020 <= eyr <= 2030:
                        c = True

            if c:
                c = False
                val = mapp['hgt']
                if val[-2:] == 'cm':
                    if representsInt(val[:3]):
                        if 150 <= int(val[:3]) <= 193:
                            c = True
                elif val[-2:] == 'in':
                    if representsInt(val[:2]):
                        if 59 <= int(val[:2]) <= 76:
                            c = True

            if c:
                c = False
                val = mapp['hcl']
                if val[0] == '#' and len(val) == 7:
                    c = True
                    for j in range(len(val) - 1):
                        tmp = ord(val[j + 1])
                        if not (48 <= tmp <= 57 or 97 <= tmp <= 102):
                            c = False
                            break

            if c:
                c = False
                val = mapp['ecl']
                if val in eyeColor:
                    c = True

            if c:
                c = False
                val = mapp['pid']
                if len(val) == 9 and representsInt(val):
                    c = True

            if c:
                res += 1
        passport = ""
    else:
        if passport == "":
            passport += inp
        else:
            passport += " " + inp

print(res)

