from pathlib import Path
from collections import deque

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().split("\n")

mid = dat.index("")
crates = dat[:mid]
instructions = dat[mid + 1 :][:-1]
nums = list(filter(("").__ne__, crates[-1].strip().split(" ")))

d = deque()

for crate in nums:
    d.append(deque())

crates = crates[:-1]

for line in crates:
    curr = 0
    for i in range(1, len(line), 4):
        d[curr].append(line[i])
        curr += 1

for i in range(len(d)):
    d[i] = list(filter((" ").__ne__, d[i]))

for line in instructions:
    p = line.split(" ")
    nu = int(p[1])
    fr = int(p[3]) - 1
    to = int(p[5]) - 1
    for i in range(nu):
        d[to].insert(0, d[fr].pop(0))

msg = ""
for line in d:
    msg += line[0]

print(msg)
