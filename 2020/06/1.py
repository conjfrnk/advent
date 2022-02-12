from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n\n")
dat = [g.split("\n") for g in dat]

s = 0
for g in dat:
    lu = dict()
    for sg in g:
        for p in sg:
            lu[p] = 1
    s += len(lu)

print(s)
