from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

import copy


def how_many_seen(dat, i, j):
    height = len(dat)
    width = len(dat[0])
    res = 0
    dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    for (di, dj) in dirs:
        ci, cj = i, j
        while True:
            ci += di
            cj += dj
            if ci < 0 or ci == height or cj < 0 or cj == width:
                break
            if dat[ci][cj] == "L":
                break
            elif dat[ci][cj] == "#":
                res += 1
                break
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
                if how_many_seen(old, i, j) == 0:
                    new[i] = new[i][:j] + "#" + new[i][j + 1 :]
            elif old[i][j] == "#":
                if how_many_seen(old, i, j) >= 5:
                    new[i] = new[i][:j] + "L" + new[i][j + 1 :]
    return new


count = 0
new_count = -1

while new_count != count:
    count = new_count
    dat = refresh(dat)
    new_count = get_occ(dat)

print(count)
