from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

size = len(dat[0])
most = [0] * size
most = ""
least = [0] * size
least = ""

for j in range(size):
    zeroes = ones = 0
    for i in range(len(dat)):
        if dat[i][j] == "0":
            zeroes += 1
        elif dat[i][j] == "1":
            ones += 1
    if ones > zeroes:
        most += "1"
        least += "0"
    else:
        most += "0"
        least += "1"

print(most)
print(least)
print(int(eval("0b" + most)) * int(eval("0b" + least)))
