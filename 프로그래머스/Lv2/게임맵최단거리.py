# def solution(maps):
#     answer = 0
#     return answer
from collections import deque
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
m = len(maps)
n = len(maps[0])
dist = [[0] * m for _ in range(n)]



dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y,maps,dist):
    q = deque()
    q.append([x,y])
    dist[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x + dx[i] , y + dy[i]   
            if 0<= nx < m and 0<= ny <n:
                if maps[nx][ny] == 1 and dist[nx][ny] == 0:
                    q.append([nx,ny])
                    dist[nx][ny] = dist[x][y] + 1
                    if nx == m-1 and ny == n-1:
                        return dist[nx][ny]

ans = bfs(0,0,maps,dist)
print(ans if ans else -1)

def solution(maps):
    from collections import deque
    n = len(maps)
    m = len(maps[0])
    dist = [[0] * m for _ in range(n)]

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    def bfs(x,y,maps,dist):
        q = deque()
        q.append([x,y])
        dist[x][y] = 1
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x + dx[i] , y + dy[i]   
                if 0<= nx < m and 0<= ny <n:
                    if maps[nx][ny] == 1 and dist[nx][ny] == 0:
                        q.append([nx,ny])
                        dist[nx][ny] = dist[x][y] + 1
                        if nx == m-1 and ny == n-1:
                            return dist[nx][ny]

    ans = bfs(0,0,maps,dist)
    return ans if ans else -1
