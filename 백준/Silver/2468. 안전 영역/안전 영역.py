import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

## 최대값 구하기
m = 0
for i in range(n):
    for j in range(n):
        if m < g[i][j]:
            m = g[i][j]

'''
이제 m이 0->1->2 .....
dfs돌려야함. 기준점 하나잡고
'''
def bfs(i,j,g,vist,rain):
    q = deque()
    q.append([i,j])
    vist[i][j] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0<= nx < n and 0<= ny <n:
                if g[nx][ny] > rain and vist[nx][ny] == 0:
                    vist[nx][ny] = 1
                    q.append([nx,ny])
        

l_cnt = []
for rain in range(m + 1): 
    vist = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] > rain and vist[i][j] == 0:
                bfs(i, j, g, vist, rain) 
                cnt += 1
    l_cnt.append(cnt)

print(max(l_cnt))