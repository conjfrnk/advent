from pathlib import Path

fn = "ex1.txt"
# fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")
