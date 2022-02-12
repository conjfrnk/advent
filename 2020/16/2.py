from pathlib import Path

# fn = "ex2.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")
import re

rules = []
i = 0

while dat[i] != "":
    rules.append(dat[i])
    i += 1

valids = dict()

for line in rules:
    first, second = line.split(": ")
    valids[first] = set()
    ranges = second.split(" or ")
    for r in ranges:
        low, high = r.split("-")
        low, high = int(low), int(high)
        for n in range(low, high + 1):
            valids[first].add(n)

i = dat.index("nearby tickets:") + 1
nearby = []

while i < len(dat):
    nearby.append(dat[i])
    i += 1

fields = len(nearby[0].split(","))
nots = dict()
for v in valids:
    nots[v] = set()

for line in nearby:
    nums = [int(n) for n in line.split(",")]
    for i in range(fields):
        adds = dict()
        num = 1
        for v in valids:
            adds[v] = set()
            if nums[i] not in valids[v]:
                adds[v].add(i)
                num += 1
        if num < fields:
            for a in adds:
                for i in adds[a]:
                    nots[a].add(i)


def invert(top, n):
    m = top
    res = set()
    while m > 0:
        m -= 1
        if m not in n:
            res.add(m)
    return res


could = dict()
for n in nots:
    could[n] = invert(fields, nots[n])


def refine(c, fin):
    def remove(c, num):
        for t in c:
            if num in c[t]:
                c[t].remove(num)

    for t in c:
        if len(c[t]) == 1:
            fin[t] = list(c[t])[0]
            remove(c, list(c[t])[0])


sol = dict()
for v in valids:
    sol[v] = None
for _ in range(fields):
    refine(could, sol)
print(sol)

inds = []

for s in sol:
    search = re.search("^departure", s)
    if search is not None:
        inds.append(sol[s])

print(inds)

mine = dat.index("your ticket:") + 1
ticket = dat[mine].split(",")
final = 1

for i in inds:
    print(ticket[i])
    final *= int(ticket[i])

print(final)
