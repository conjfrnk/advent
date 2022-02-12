from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

import re

regex = re.compile("(\d*)-(\d*)\s(\w):\s(\w*)")
one = 0
two = 0
for line in dat:
    first, second, char, pw = regex.findall(line)[0]
    first = int(first)
    second = int(second)

    # part one
    chars = pw.count(char)
    if chars >= first and chars <= second:
        one += 1

    # part two
    if pw[first - 1] == char and pw[second - 1] != char:
        two += 1
    elif pw[first - 1] != char and pw[second - 1] == char:
        two += 1

print("first:", one)
print("second:", two)
