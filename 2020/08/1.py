from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

for i in range(len(dat)):
    dat[i] = dat[i].split(" ")

i = 0
acc = 0
done = set()
while True:
    if i in done:
        break
    done.add(i)
    if dat[i][0] == "nop":
        i += 1
    elif dat[i][0] == "acc":
        acc += eval(dat[i][1])
        i += 1
    elif dat[i][0] == "jmp":
        i += eval(dat[i][1])

print(acc)
