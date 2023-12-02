from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

ans = 0

for n, line in enumerate(dat):
    _, rounds = line.split(":")
    mset = {"red": 0, "green": 0, "blue": 0}
    for r in rounds.split(";"):
        for ncubes in r.split(","):
            n, c = ncubes.strip().split(" ")
            n = int(n)
            if n > mset[c]:
                mset[c] = n
    power = 1
    for c in mset:
        power *= mset[c]
    ans += power

print(ans)
