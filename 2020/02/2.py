from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

import re

regex = re.compile("(\d*)-(\d*)\s(\w):\s(\w*)")
res = 0
for line in dat:
    first, second, char, pw = regex.findall(line)[0]
    first, second = int(first), int(second)

    if pw[first - 1] == char and pw[second - 1] != char:
        res += 1
    elif pw[first - 1] != char and pw[second - 1] == char:
        res += 1

print(res)
