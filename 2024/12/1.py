from pathlib import Path

# fn = "ex3.txt"
fn = "input.txt"
fn = Path(Path(__file__).parent, fn)
dat = open(fn).read().strip().split("\n")

grid = dat
n = len(grid)
m = len(grid[0])
visited = [[False]*m for _ in range(n)]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]
res = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            c = grid[i][j]
            stack = [(i,j)]
            visited[i][j] = True
            cells = []
            while stack:
                x,y = stack.pop()
                cells.append((x,y))
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny]==c:
                        visited[nx][ny] = True
                        stack.append((nx,ny))
            area = len(cells)
            perimeter = 0
            for x,y in cells:
                for dx,dy in dirs:
                    nx,ny = x+dx,y+dy
                    if not (0<=nx<n and 0<=ny<m and grid[nx][ny]==c):
                        perimeter+=1
            res += area*perimeter

print(res)
