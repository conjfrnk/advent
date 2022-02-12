from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n\n")
dat = [g.split("\n") for g in dat]

s = 0
for g in dat:
    lu = dict()
    for p in g:
        for q in p:
            if q not in lu:
                lu[q] = []
            lu[q].append(p)
    for q in lu:
        if len(lu[q]) == len(g):
            s += 1

print(s)
