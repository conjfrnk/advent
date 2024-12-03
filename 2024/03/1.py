from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip()

import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
matches = re.finditer(pattern, dat)
total = 0
for match in matches:
    x = int(match.group(1))
    y = int(match.group(2))
    result = x * y
    total += result

print(total)
