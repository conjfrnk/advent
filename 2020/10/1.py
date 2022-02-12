from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

import copy

dev = 0

for i in range(len(dat)):
    dat[i] = int(dat[i])
    if dat[i] > dev:
        dev = dat[i]

dev += 3

diff_1 = 0
diff_3 = 0

ads = copy.copy(dat)
ads.append(0)
ads.append(dev)
ads = sorted(ads)
for i in range(len(ads) - 1):
    cur = ads[i]
    nex = ads[i + 1]
    diff = nex - cur
    if diff == 1:
        diff_1 += 1
    elif diff == 3:
        diff_3 += 1

print(diff_1, diff_3)
ans = diff_1 * diff_3
print(ans)
