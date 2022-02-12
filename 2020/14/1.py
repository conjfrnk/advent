from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

memory = {}
masks = []
c_mask = c_val = c_addr = None

for line in dat:
    k, v = line.split(" = ")
    if k == "mask":
        masks.append(v)
        c_mask = v
    else:
        c_addr = int(k[4:-1])
        c_val = int(v)
        binval = list(bin(c_val)[2:].zfill(36))
        n_val = [0] * 36

        for i, (mask, value) in enumerate(zip(c_mask, binval)):
            if mask == "X":
                n_val[i] = value
            else:
                n_val[i] = mask

        memory[c_addr] = int("".join(n_val), 2)

print(sum(memory.values()))
