from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")
dat = set([int(line) for line in dat])

for e in dat:
    if 2020 - e in dat:
        one = e * (2020 - e)
        break

print(one)
