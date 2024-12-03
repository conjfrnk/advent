from pathlib import Path

# fn = "ex2.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip()

import re

mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"

total = 0
enabled = True
current_pos = 0

while current_pos < len(dat):
    do_match = re.match(do_pattern, dat[current_pos:])
    dont_match = re.match(dont_pattern, dat[current_pos:])
    if do_match:
        enabled = True
        current_pos += do_match.end()
        continue
    elif dont_match:
        enabled = False
        current_pos += dont_match.end()
        continue
    mul_match = re.match(mul_pattern, dat[current_pos:])
    if mul_match and enabled:
        x = int(mul_match.group(1))
        y = int(mul_match.group(2))
        total += x * y
    current_pos += 1 if not mul_match else mul_match.end()

print(total)
