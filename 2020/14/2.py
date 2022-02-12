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
        b_add = list(bin(c_addr)[2:].zfill(36))
        n_add = ["0"] * 36

        v = len(list(bin(c_addr)[2:]))

        for i, (mask, val) in enumerate(zip(c_mask, b_add)):
            if mask == "X":
                n_add[i] = "X"
            elif mask == "0":
                n_add[i] = val
            elif mask == "1":
                n_add[i] = "1"

        n_add = "".join(n_add)
        n_poss = n_add.count("X")

        flucts = []
        for i in range(2 ** n_poss):
            flucts.append(list(bin(i)[2:].zfill(n_poss)))

        for fluct in flucts:
            i = 0
            nadd = ""
            for a in n_add:
                if a == "X":
                    nadd += str(fluct[i])
                    i += 1
                else:
                    nadd += str(a)
            memory[int(nadd, 2)] = c_val

print(sum(memory.values()))
