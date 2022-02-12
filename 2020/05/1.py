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


max_id = 0
for s in dat:
    row = getPart(s[0:7], 0, 127)
    col = getPart(s[7:], 0, 7)
    seat_id = (row * 8) + col
    if seat_id > max_id:
        max_id = seat_id

print(max_id)
