"""NOTE: this approach takes forever..."""

from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

nums = []

for num in dat[0].split(","):
    nums.append(int(num))

counts = dict()

for i, num in enumerate(nums):
    counts[str(num)] = []
    counts[str(num)].append(i + 1)

TURNS = 30000000

for i in range(len(nums), TURNS):
    print(i, end="\r")
    last = nums[i - 1]
    if str(last) not in counts:
        counts[str(last)] = []
        counts[str(last)].append(i)
        counts[str(0)].append(i + 1)
        nums.append(0)
    elif len(counts[str(last)]) == 1:
        counts[str(0)].append(i + 1)
        nums.append(0)
    else:
        res = counts[str(last)][-1] - counts[str(last)][-2]
        if str(res) not in counts:
            counts[str(res)] = []
        counts[str(res)].append(i + 1)
        nums.append(res)

print()
print(nums[TURNS - 1])
