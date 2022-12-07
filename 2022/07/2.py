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

used = 70000000 - 30000000
total = SZ["/"]
need = total - used

res = 1e9

for k, v in SZ.items():
    if v >= need:
        res = min(res, v)

print(res)
