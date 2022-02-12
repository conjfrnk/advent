from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n\n")

tiles = dict()

for tile in dat:
    broken = tile.strip("\n").split("\n")
    num = int(broken[0].split()[1].strip(":"))
    arr = broken[1:]
    sides = [
        arr[0],
        arr[-1],
        "".join([a[0] for a in arr]),
        "".join([a[-1] for a in arr]),
    ]
    sides += [s[::-1] for s in sides]
    tiles[num] = dict()
    tiles[num]["arr"] = arr
    tiles[num]["sides"] = sides
    tiles[num]["bordering"] = dict()

    for i, tile in tiles.items():
        if i == num:
            continue
        borders = [s for s in tile["sides"] if s in sides]
        for b in borders:
            tiles[num]["bordering"][i] = b
            tiles[i]["bordering"][num] = b

toplevelarr = list(map(int, [t for t in tiles if len(tiles[t]["bordering"]) == 2]))
sol = 1
for c in toplevelarr:
    sol *= c

print(sol)
