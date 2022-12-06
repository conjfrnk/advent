from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

res = 0
line = dat[0]


def check(s):
    counts = dict()
    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] += 1
        if counts[c] > 1:
            return False
    return True


seen = set()
req = 4

for i in range(req, len(line)):
    if check(line[i - req : i]):
        res = i
        break

print(res)
