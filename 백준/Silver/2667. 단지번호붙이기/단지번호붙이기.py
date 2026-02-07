"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

"""

import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
g = [list(input().strip()) for _ in range(n)]
v = [list([0]*n) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(i,j,g,v):
    q = deque()
    q.append([i,j])
    v[i][j] = 1
    c = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if g[nx][ny] == "1" and v[nx][ny] == 0:
                    v[nx][ny] = 1
                    q.append([nx,ny])
                    c+=1
    return c

# 전체 단지 개수
cnt = 0

# 단지내 아파트 수
l = []
for i in range(n):
    for j in range(n):
        if v[i][j] == 0 and g[i][j] == "1":
            l.append(bfs(i,j,g,v)) #여기서 반환되야하는 값 : 단지 내 아파트 수
            cnt += 1
l.sort()
print(cnt)
for i in l:
    print(i)