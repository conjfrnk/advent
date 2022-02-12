from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

import copy

for i in range(len(dat)):
    dat[i] = dat[i].split(" ")


def test(dat, i, val):
    dat[i] = (val, dat[i][1])
    i = 0
    acc = 0
    visited = set()
    while True:
        if i == len(dat):
            return True
        if i in visited:
            return False
        visited.add(i)
        delta = eval(dat[i][1])
        if dat[i][0] == "nop":
            i += 1
        elif dat[i][0] == "acc":
            acc += delta
            i += 1
        elif dat[i][0] == "jmp":
            i += delta


i = 0
acc = 0
while True:
    if i == len(dat):
        break
    delta = eval(dat[i][1])
    if dat[i][0] == "nop":
        if test(copy.copy(dat), i, "jmp"):
            i += delta
        else:
            i += 1
    elif dat[i][0] == "acc":
        acc += delta
        i += 1
    elif dat[i][0] == "jmp":
        if test(copy.copy(dat), i, "nop"):
            i += 1
        else:
            i += delta

print(acc)
