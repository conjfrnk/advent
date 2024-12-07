from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

import itertools

res = 0
for line in dat:
    left, right = line.split(":")
    val = int(left.strip())
    nums = list(map(int, right.strip().split()))
    if len(nums) == 1:
        if nums[0] == val:
            res += val
        continue
    ops_slots = len(nums) - 1
    can = False
    for pattern in itertools.product(["+", "*"], repeat=ops_slots):
        total = nums[0]
        for op, n in zip(pattern, nums[1:]):
            if op == "+":
                total = total + n
            else:
                total = total * n
        if total == val:
            can = True
            break
    if can:
        res += val

print(res)
