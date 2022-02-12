from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

for i in range(len(dat)):
    dat[i] = int(dat[i])

pre = 25

for i in range(pre, len(dat)):
    flag = False
    for j in range(i - pre, i):
        for k in range(i - pre, i):
            if j == k:
                break
            if dat[j] + dat[k] == dat[i]:
                flag = True
    if not flag:
        print(dat[i])
        exit(0)
