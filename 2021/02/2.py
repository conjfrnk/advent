from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

horiz = 0
depth = 0
aim = 0

for line in dat:
    word, num = line.split(" ")
    num = int(num)
    if word == "forward":
        horiz += num
        depth += aim * num
    elif word == "down":
        aim += num
    elif word == "up":
        aim -= num

print(horiz * depth)
