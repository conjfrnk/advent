from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

safe_count = 0

for line in dat:
    nums = [int(x) for x in line.split(" ")]
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
    if flag:
        safe_count += 1

print(safe_count)
