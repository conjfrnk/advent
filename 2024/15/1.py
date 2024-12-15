from pathlib import Path

#fn = "ex1.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

grid = []
moves = []
for line in dat:
    if line.startswith("#"):
        grid.append(list(line))
    else:
        moves.append(line)
moves = "".join(moves)

R = len(grid)
C = len(grid[0])
for r in range(R):
    for c in range(C):
        if grid[r][c] == '@':
            rr, cc = r, c

dirs = {'^':(-1,0),'v':(1,0),'<':(0,-1),'>':(0,1)}
for m in moves:
    dr, dc = dirs[m]
    nr, nc = rr+dr, cc+dc
    if grid[nr][nc] == '#':
        continue
    if grid[nr][nc] == 'O':
        chain = []
        rr2, cc2 = nr, nc
        while 0<=rr2<R and 0<=cc2<C and grid[rr2][cc2]=='O':
            chain.append((rr2,cc2))
            rr2 += dr
            cc2 += dc
        if grid[rr2][cc2] != '.':
            continue
        grid[rr][cc] = '.'
        rr, cc = rr+dr, cc+dc
        grid[rr][cc] = '@'
        for i in reversed(range(len(chain))):
            r2, c2 = chain[i]
            grid[r2][c2] = '.'
            grid[r2+dr][c2+dc] = 'O'
    else:
        grid[rr][cc] = '.'
        rr, cc = nr, nc
        grid[rr][cc] = '@'

boxes = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == 'O':
            boxes.append(100*r + c)
print(sum(boxes))
