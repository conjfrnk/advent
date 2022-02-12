from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

buses = dat[1].split(",")

mods = {}
for idx, bus in enumerate(buses):
    if bus != "x":
        mods[bus] = -idx % int(bus)

i = 0
inc = 1
for bus in mods.keys():
    while i % int(bus) != mods[bus]:
        i += inc
    inc *= int(bus)

print(i)
