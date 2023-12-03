from pathlib import Path
import json

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

ans = 0
nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
invalid = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."}
in_num = False
is_valid = False
curr_num = ""
curr_gear = []
gears = []

for i in range(len(dat)):
    for j in range(len(dat[i])):
        if not in_num:
            if is_valid:
                gears.append((curr_gear, curr_num))
            is_valid = False
            curr_num = ""
        in_num = dat[i][j] in nums
        if in_num:
            curr_num += str(dat[i][j])
            # search up
            if i != 0 and dat[i - 1][j] == "*":
                curr_gear = [i - 1, j]
                is_valid = True
            # search down
            if i != len(dat) - 1 and dat[i + 1][j] == "*":
                curr_gear = [i + 1, j]
                is_valid = True
            # search left
            if j != 0 and dat[i][j - 1] == "*":
                curr_gear = [i, j - 1]
                is_valid = True
            # search right
            if j != len(dat[0]) - 1 and dat[i][j + 1] == "*":
                curr_gear = [i, j + 1]
                is_valid = True
            # search diagonal up/left
            if i != 0 and j != 0 and dat[i - 1][j - 1] == "*":
                curr_gear = [i - 1, j - 1]
                is_valid = True
            # search down/left
            if i != len(dat) - 1 and j != 0 and dat[i + 1][j - 1] == "*":
                curr_gear = [i + 1, j - 1]
                is_valid = True
            # search diagonal up/right
            if i != 0 and j != len(dat[0]) - 1 and dat[i - 1][j + 1] == "*":
                curr_gear = [i - 1, j + 1]
                is_valid = True
            # search down/right
            if i != len(dat) - 1 and j != len(dat[0]) - 1 and dat[i + 1][j + 1] == "*":
                curr_gear = [i + 1, j + 1]
                is_valid = True

counts = dict()

for gear in gears:
    pos, num = gear[0], gear[1]
    if str(pos) not in counts:
        counts[str(pos)] = 0
    counts[str(pos)] += 1

for pos in counts:
    if counts[pos] == 2:
        curr = 1
        for g in gears:
            loc = json.loads(pos)
            if g[0][0] == loc[0] and g[0][1] == loc[1]:
                curr *= int(g[1])
        ans += curr

print(ans)
