from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    vist = [[0] * m for _ in range(n)]

    def bfs(x,y):
        q = deque()
        q.append([x,y])
        vist[x][y] = 1
        temp = int(maps[x][y])
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i] , y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if vist[nx][ny] == 0 and maps[nx][ny] != "X":
                        vist[nx][ny] = 1
                        temp += int(maps[nx][ny])
                        q.append([nx,ny])
        return temp

    result = []
    for i in range(n):
        for j in range(m):
            if vist[i][j] == 0 and maps[i][j] != "X":
                result.append(bfs(i,j))

    if len(result) == 0:
        result.append(-1)

    result.sort()

    return result

















from collections import deque
maps = ["X591X","X1X5X","X231X", "1XXX1"]
n = len(maps)
m = len(maps[0])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

vist = [[0] * m for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    vist[x][y] = 1
    temp = int(maps[x][y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if vist[nx][ny] == 0 and maps[nx][ny] != "X":
                    vist[nx][ny] = 1
                    temp += int(maps[nx][ny])
                    q.append([nx,ny])
    return temp



result = []
for i in range(n):
    for j in range(m):
        if vist[i][j] == 0 and maps[i][j] != "X":
            result.append(bfs(i,j))

if len(result) == 0:
    result.append(-1)

result.sort()
print(result)
