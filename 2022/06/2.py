from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")


def check(s):
    counts = set()
    for c in s:
        if c not in counts:
            counts.add(c)
        else:
            return False
    return True


line = dat[0]
req = 14

for i in range(req, len(line)):
    if check(line[i - req : i]):
        print(i)
        break
