from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

import copy


def get_adj(dat, i, j):
    height = len(dat)
    width = len(dat[0])
    res = 0
    for di in range(-1, 2):
        new_i = i + di
        if new_i < 0 or new_i >= height:
            continue
        for dj in range(-1, 2):
            new_j = j + dj
            if new_j < 0 or new_j >= width or (i, j) == (new_i, new_j):
                continue
            if dat[new_i][new_j] == "#":
                res += 1
    return res


def get_occ(dat):
    count = 0
    for line in dat:
        for char in line:
            if char == "#":
                count += 1
    return count


def refresh(old):
    new = copy.copy(old)
    height = len(old)
    width = len(old[0])
    for i in range(height):
        for j in range(width):
            if old[i][j] == "L":
                if get_adj(old, i, j) == 0:
                    new[i] = new[i][:j] + "#" + new[i][j + 1 :]
            elif old[i][j] == "#":
                if get_adj(old, i, j) >= 4:
                    new[i] = new[i][:j] + "L" + new[i][j + 1 :]
    return new


def printer(dat):
    print()
    for line in dat:
        print(line)


count = 0
new_count = -1

while new_count != count:
    count = new_count
    dat = refresh(dat)
    new_count = get_occ(dat)

print(count)
