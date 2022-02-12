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

    chars = pw.count(char)
    if chars >= first and chars <= second:
        res += 1

print(res)
