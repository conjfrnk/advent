from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")


def getPart(s, n0, n1):
    if not s:
        return n1
    if s[0] == "F" or s[0] == "L":
        return getPart(s[1:], n0, (n0 + n1) // 2)
    else:
        return getPart(s[1:], n0 + ((n1 - n0) // 2), n1)


min_id = 1000
max_id = 0
ids = dict()
for s in dat:
    row = getPart(s[0:7], 0, 127)
    col = getPart(s[7:], 0, 7)
    seat_id = (row * 8) + col
    if seat_id < min_id:
        min_id = seat_id
    if seat_id > max_id:
        max_id = seat_id
    ids[seat_id] = 1

for i in range(min_id, max_id + 1):
    if i not in ids:
        print(i)
