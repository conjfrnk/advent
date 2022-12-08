from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

res = 2 * (2 * len(dat) - 2)

for i in range(1, len(dat) - 1):
    flag = True
    for j in range(1, len(dat[i]) - 1):
        curr = int(dat[i][j])
        for di in range(i):
            if int(dat[di][j]) >= curr:
                flag = False
                break
        if flag:
            res += 1
            continue
        flag = True
        for di in range(i + 1, len(dat)):
            if int(dat[di][j]) >= curr:
                flag = False
                break
        if flag:
            res += 1
            continue
        flag = True
        for dj in range(j):
            if int(dat[i][dj]) >= curr:
                flag = False
                break
        if flag:
            res += 1
            continue
        flag = True
        for dj in range(j + 1, len(dat[i])):
            if int(dat[i][dj]) >= curr:
                flag = False
                break
        if flag:
            res += 1
            continue
        flag = True

print(res)
