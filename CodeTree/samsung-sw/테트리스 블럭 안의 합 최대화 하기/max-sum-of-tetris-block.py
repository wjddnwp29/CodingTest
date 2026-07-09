n, m = map(int,input().split())

g = [list(map(int,input().split())) for i in range(n)]
vist = [[False] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]


ans = 0
def dfs(x,y,depth, tmp):
    if depth == 4:
        global ans
        ans = max(ans,tmp)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m and not vist[nx][ny]:


                if depth == 2:
                    vist[nx][ny] = True
                    dfs(x,y,depth+1,tmp+g[nx][ny])
                    vist[nx][ny] = False

                vist[nx][ny] = True
                dfs(nx,ny,depth+1,tmp+g[nx][ny])
                vist[nx][ny] = False


for i in range(n):
    for j in range(m):
        vist[i][j] = True
        dfs(i,j,1,g[i][j])
        vist[i][j] = False
print(ans)