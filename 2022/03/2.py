from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

elves = []

for i in range(0, len(dat), 3):
    new = []
    for j in range(3):
        new.append(dat[i + j])
    elves.append(new)

commons = ""

for group in elves:
    common = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

    for line in group:
        common &= set(line)

    commons += list(common)[0]

res = 0

for char in commons:
    num = ord(char.lower()) - 96
    if char.isupper():
        num += 26
    res += num

print(res)
