from collections import deque
n, L, R = map(int,input().split())
g = [list(map(int,input().split())) for i in range(n)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,vist,cnt,idx,group):
    cnt += 1
    tmp = g[x][y]
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+ dy[i]
            if 0<=nx<n and 0<=ny<n:
                if vist[nx][ny] == False:
                    if L <= abs(g[x][y] - g[nx][ny]) and abs(g[x][y] - g[nx][ny]) <= R:
                        vist[nx][ny] = True
                        tmp += g[nx][ny]
                        group[nx][ny] = idx
                        q.append([nx,ny])
                        cnt += 1
    return tmp//cnt

ans = 0
while 1:
    vist = [[False] * n for i in range(n)]
    group = [[0] * n for i in range(n)]
    cnt = 0
    t = []
    idx = 0
    for i in range(n):
        for j in range(n):
            if vist[i][j] == False:
                vist[i][j] = True
                group[i][j] = idx
                avg = bfs(i,j,vist,cnt,idx,group)
                t.append(avg)
                cnt = 0
                idx += 1

    if len(t) == n*n:
        break

    for i in range(n):
        for j in range(n):
            x = group[i][j]
            g[i][j] = t[x]
    ans += 1


print(ans)


'''
3 15 24
20 25 40
30 50 40
10 30 45

3 15 30
10 45 40
45 40 45
10 5 10
'''




