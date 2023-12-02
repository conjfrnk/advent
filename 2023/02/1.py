from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

ans = 0

maxes = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def possible(r):
    for ncubes in r.split(","):
        n, c = ncubes.strip().split(" ")
        if int(n) > maxes[c]:
            return False
    return True


for n, line in enumerate(dat):
    _, rounds = line.split(":")
    flag = True
    for r in rounds.split(";"):
        if not possible(r):
            flag = False
    if flag:
        ans += n + 1

print(ans)
