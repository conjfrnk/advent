from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n\n")

for i in range(len(dat)):
    dat[i] = dat[i].split("\n")
    for j in range(len(dat[i])):
        dat[i][j] = dat[i][j].split(" ")

need = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


valid = 0
for port in dat:
    lu = dict()
    for line in port:
        for field in line:
            key, val = field.split(":")
            if key == "byr" and 1920 <= int(val) <= 2002:
                lu[key] = val
            elif key == "iyr" and 2010 <= int(val) <= 2020:
                lu[key] = val
            elif key == "eyr" and 2020 <= int(val) <= 2030:
                lu[key] = val
            elif key == "hgt":
                if val[-2:] == "cm" and 150 <= int(val[:-2]) <= 193:
                    lu[key] = val
                elif val[-2:] == "in" and 59 <= int(val[:-2]) <= 76:
                    lu[key] = val
            elif key == "hcl":
                if val[0] == "#" and len(val) == 7:
                    flag = True
                    for c in val[1:]:
                        if c not in "0123456789abcdef":
                            flag = False
                    if flag:
                        lu[key] = val
            elif key == "ecl":
                if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    lu[key] = val
            elif key == "pid" and len(val) == 9:
                lu[key] = val
    for f in need:
        if f not in lu:
            valid -= 1
            break
    valid += 1

print(valid)
