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
            lu[key] = val
    for f in need:
        if f not in lu:
            valid -= 1
            break
    valid += 1

print(valid)
