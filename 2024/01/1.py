from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

l1 = []
l2 = []

# make two sorted lists
for line in dat:
    n1 = line.split(" ")[0]
    n2 = line.split(" ")[-1]
    l1.append(int(n1))
    l2.append(int(n2))

l1.sort()
l2.sort()

# find differences
tot = 0
for i in range(len(l1)):
    tot += abs(l1[i] - l2[i])

# print total difference
print(tot)
