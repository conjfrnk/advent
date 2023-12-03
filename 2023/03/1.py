from pathlib import Path

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
valids = []

for i in range(len(dat)):
    for j in range(len(dat[i])):
        if not in_num:
            if is_valid:
                valids.append(curr_num)
            is_valid = False
            curr_num = ""
        in_num = dat[i][j] in nums
        if in_num:
            curr_num += str(dat[i][j])
            # search up
            if i != 0 and dat[i - 1][j] not in invalid:
                is_valid = True
            # search down
            if i != len(dat) - 1 and dat[i + 1][j] not in invalid:
                is_valid = True
            # search left
            if j != 0 and dat[i][j - 1] not in invalid:
                is_valid = True
            # search right
            if j != len(dat[0]) - 1 and dat[i][j + 1] not in invalid:
                is_valid = True
            # search diagonal up/left
            if i != 0 and j != 0 and dat[i - 1][j - 1] not in invalid:
                is_valid = True
            # search down/left
            if i != len(dat) - 1 and j != 0 and dat[i + 1][j - 1] not in invalid:
                is_valid = True
            # search diagonal up/right
            if i != 0 and j != len(dat[0]) - 1 and dat[i - 1][j + 1] not in invalid:
                is_valid = True
            # search down/right
            if i != len(dat) - 1 and j != len(dat[0]) - 1 and dat[i + 1][j + 1] not in invalid:
                is_valid = True

for num in valids:
    ans += int(num)

print(ans)
