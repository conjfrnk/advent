from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")
dat = set([int(line) for line in dat])

two = False
lu = set(dat)
for e1 in dat:
    remain = 2020 - e1
    for e2 in dat:
        if remain - e2 in lu and e2 != e1:
            two = e1 * e2 * (remain - e2)
            break
        if two:
            break

print(two)
