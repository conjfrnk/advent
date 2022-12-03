from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

part1 = []
part2 = []

for line in dat:
    mid = len(line) // 2
    part1.append(line[:mid])
    part2.append(line[mid:])

commons = ""

for i in range(len(part1)):
    s1 = part1[i]
    s2 = part2[i]
    common = list(set(s1) & set(s2))
    commons += common[0]

res = 0

for char in commons:
    num = ord(char.lower()) - 96
    if char.isupper():
        num += 26
    res += num

print(res)
