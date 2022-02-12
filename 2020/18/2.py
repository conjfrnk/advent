from pathlib import Path

# fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")


class Num:
    def __init__(self, i):
        self.i = i

    def __add__(self, x):
        return Num(self.i * x.i)

    def __mul__(self, x):
        return Num(self.i + x.i)

    def __sub__(self, x):
        return Num(self.i * x.i)


def my_eval(x):
    s = ""
    in_num = False
    for c in x:
        if c in "1234567890" and in_num == False:
            s += "Num("
            in_num = True
        if in_num == True and c not in "1234567890":
            s += ")"
            in_num = False
        s += c
    if in_num:
        s += ")"
    return eval(s).i


acc = 0
for x in dat:
    acc += my_eval(x.replace("*", "-").replace("+", "*").replace("-", "+"))
print(acc)
