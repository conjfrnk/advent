from pathlib import Path
from collections import defaultdict

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

SZ = defaultdict(int)
path = []
for line in dat:
    words = line.strip().split()
    if words[1] == "cd":
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == "ls":
        continue
    elif words[0] == "dir":
        continue
    else:
        sz = int(words[0])
        for i in range(1, len(path) + 1):
            SZ["/".join(path[:i])] += sz

res = 0

for k, v in SZ.items():
    if v <= 100000:
        res += v

print(res)
