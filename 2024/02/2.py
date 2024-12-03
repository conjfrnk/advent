import copy
from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

safe_count = 0


def test_nums(nums):
    flag = True
    positive = True
    for i in range(len(nums) - 1):
        n1 = nums[i]
        n2 = nums[i + 1]
        diff = n1 - n2
        if diff > 0:
            new_pos = True
        else:
            new_pos = False
        if i == 0:
            positive = new_pos
        if positive != new_pos:
            flag = False
            break
        if not 1 <= abs(diff) <= 3:
            flag = False
            break
    return flag


for line in dat:
    nums = [int(x) for x in line.split(" ")]
    if test_nums(nums):
        safe_count += 1
    else:
        for i in range(len(nums)):
            nums_copy = copy.copy(nums)
            nums_copy.pop(i)
            if test_nums(nums_copy):
                safe_count += 1
                break

print(safe_count)
