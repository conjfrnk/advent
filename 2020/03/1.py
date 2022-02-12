from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

mult = (len(dat) // len(dat[0])) * 4
dat = [line * mult for line in dat]

trees = 0
j = 0
for i in range(0, len(dat), 1):
    curr = dat[i][j]
    if curr == "#":
        trees += 1
    j += 3
print(trees)
