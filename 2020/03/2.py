from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

# right, down
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

mult = (len(dat) // len(dat[0])) * max([sum(s) for s in slopes])
dat = [line * mult for line in dat]

tList = []

for s in slopes:
    dj, di = s[0], s[1]
    trees = 0
    j = 0
    for i in range(0, len(dat), di):
        curr = dat[i][j]
        if curr == "#":
            trees += 1
        j += dj
    tList.append(trees)

print("tree hits:", tList)

prod = 1
for t in tList:
    prod *= t
print(prod)
