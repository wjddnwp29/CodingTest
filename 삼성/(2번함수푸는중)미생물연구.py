'''
8 4
2 2 5 6
2 3 5 8
2 0 5 3
1 1 6 6
'''
from collections import deque
n, q = map(int,input().split())
g = [[-1]* (n) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs_count(g,vist,row,col):
    q = deque()
    q.append([row,col])
    vist[row][col] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not vist[nx][ny] and g[nx][ny] == g[row][col]:
                    vist[nx][ny] = True
                    q.append([nx,ny])
    return g[row][col]



#1) 미생물 투입
def put_mi(index,g,r1,c1,r2,c2):
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            g[i][j] = index

    temp_list = [[0]*n]
    vist = [[False] * (n) for _ in range(n)]
    ## 이제 여기서 bfs돌면서 각 그룹이 몇개인지를 찾아야함.
    for row in range(n):
        for col in range(n):
            # -1 아닐떄만 들어가야함.
            if g[row][col] == -1:
                vist[row][col] = True
            elif g[row][col] != -1:
                if not vist[row][col]:
                    temp = bfs_count(g, vist, row, col)
                    temp_list[0][temp] += 1

    ## 그룹은 찾음 이제 삭제해야함.
    for r in range(n):
        for c in range(n):
            if temp_list[0][g[r][c]] >= 2:
                g[r][c] = -1

# #2) 배양용기 이동
def move_mi(g):
    # 이제 새로운거 할당할 새 맵
    new_g = [[0]*n for _ in range(n)]
    ## 먼저 일단 여기다가 찾아야함. 뭐를 ? 행렬 왼쪽끝 오른쪽끝 즉 그룹을 찾아야함. 뭐로 bfs로 찾아야함.
    ## 그러면 bfs로 찾으면서 -> 이걸로 할필요없음 for문 돌리면됨.
    ## 자기 위쪽이랑 다르면 그게 행값
    ## 자기 왼쪽이랑 다르면 그게 열값
    ## 자기 위쪽이랑 다르면 그게 행값
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(n):
        for j in range(n):






def bfs_count2(g,vist,row,col):
    q = deque()
    q.append([row,col])
    vist[row][col] = True
    cnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i] , y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if not vist[nx][ny] and g[nx][ny] == g[row][col]:
                    vist[nx][ny] = True
                    q.append([nx,ny])
                    cnt += 1
    return cnt

#3) 실험 결과 출력
def print_ans(g):
    vist = [[False] * (n) for _ in range(n)]
    # 3-1) 얘는 이미 정렬된 상태 -> 각 그룹별 개수 count 하고
    temp_count = [[0]*n]
    for i in range(n):
        for j in range(n):
            # -1 아닐떄만 들어가야함.
            if g[i][j] == -1:
                vist[i][j] = True
            elif g[i][j] != -1:
                if not vist[i][j]:
                    temp_count[0][g[i][j]] = bfs_count2(g, vist, i, j)

    # 3-2) 주변애 있는 그룹을 체크해야함. 그러면 주변에 있는애들로 계산해서 답 리턴
    ## set로 ?? -> 이렇게 체크하면 1 2 3 이렇게나올수도있음.. 그러면 있는거 뽑아내면서 순서대로 계산하면 okay
    ## 밑으로도 체크해야함 . ㅇㅇ 그러면 okay 해결할수도있을거같음.

    p = set()

    for i in range(n):
        row_data = []
        for j in range(n):
            if g[i][j] not in row_data and g[i][j] != -1:
                row_data.append(g[i][j])

        for s in range(len(row_data) - 1):
            p.add(tuple([row_data[s],row_data[s+1]]))

    for j in range(n):
        col_data = []
        for i in range(n):
            if g[i][j] not in col_data and g[i][j] != -1:
                col_data.append(g[i][j])

        for s in range(len(col_data)-1):
            p.add(tuple([col_data[s],col_data[s+1]]))

    list_ans = [list(x) for x in p]

    ans = 0
    if len(list_ans) > 0:
        for x,y in list_ans:
            ans += temp_count[0][x] * temp_count[0][y]
    print(ans)



#4) 전체 실험
for index in range(q):
    r1, c1, r2, c2 = map(int,input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    #1) 미생물투입 걍 넣기만 하면되네 있든말든
    put_mi(index,g,r1,c1,r2,c2)
    #2) 배양 용기 이동
    # move_mi(g)
    #3) 실험 결과 출력
    print_ans(g)





