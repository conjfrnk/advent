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

counts = dict()

for n in l2:
    if n not in counts:
        counts[n] = 1
    else:
        counts[n] += 1

# find differences
tot = 0
for i in range(len(l1)):
    if l1[i] in counts:
        tot += l1[i] * counts[l1[i]]

# print total difference
print(tot)
