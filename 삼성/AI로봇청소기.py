from collections import deque
n, k, l = map(int,input().split())

# 먼지
g = [list(map(int,input().split())) for _ in range(n)]

clean_unit = []
for i in range(k):
    x, y = map(int,input().split())
    clean_unit.append([x-1,y-1])

# 1) 청소기 이동
'''
이동거리가 가장 가까운 오염된 격자로 이동
물건이 위치하거나 청소기가 있으면 이동불가
가장 가까운 격자가 여러 개일 경우 행 번호가 작은 격자로 이동 => 열 번호가 작은 격자로 이동
'''
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def move_unit(g,start_x,start_y):
    v = [[False] * n for _ in range(n)]
    q = deque()
    q.append([start_x,start_y,0])
    v[start_x][start_y] = True

    set_unit = set((x,y) for x,y in clean_unit)

    min_dist = float('inf')
    temp = []

    while q:
        x, y, dist = q.popleft()
        if dist > min_dist:
            break
        if g[x][y] > 0:
            temp.append([x,y])
            min_dist = dist
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and not v[nx][ny]:
                if g[nx][ny] != -1 and (nx,ny) not in set_unit:
                    q.append([nx,ny,dist+1])
                    v[nx][ny] = True
    if temp:
        temp.sort()
        return temp[0][0], temp[0][1]
    else:
        return start_x, start_y

# 2) 청소
'''
청소기가 바로보고 있는 방향으로 자기 뒤에꺼 제외 청소가능
but 청소할 수 있는 최대 먼지량 20
오른쪽부터 시계방향으로
청소기 순서대로 진행
'''
dx_clean = [0, 1, 0, -1]
dy_clean = [1, 0, -1, 0]
def clean_dust(g,start_x,start_y):
    '''
    총 4번 돌면서 비교해야하는 것들
    1) 20안넘는 max 먼지값
    2) 바라보는 방향이 어디인지


    ## 끝나고해야하는것
    그 방향대로 청소
    '''
    dust = -1
    d = -1
    for i in range(4):
        temp = 0
        b_d = (i+2) % 4

        if g[start_x][start_y] > 0:
            temp += min(20,g[start_x][start_y])

        for j in range(4):
            if j == b_d:
                continue
            nx, ny = start_x + dx_clean[j], start_y + dy_clean[j]
            if 0<=nx<n and 0<=ny<n:
                if g[nx][ny] > 0:
                    temp += min(20,g[nx][ny])
        
        if temp > dust:
            dust = temp
            d = i
    
    # 끝났으니 청소해야함
    if d != -1:
        ## 내꺼부터
        if g[start_x][start_y] > 0:
            g[start_x][start_y] = max(0,g[start_x][start_y]-20)
        
        back_d = (d+2)%4
        for s in range(4):
            if s == back_d:
                continue
            nx, ny = start_x + dx_clean[s], start_y + dy_clean[s]
            if 0<=nx<n and 0<=ny<n:
                if g[nx][ny] > 0:
                    g[nx][ny] = max(0,g[nx][ny]-20)
    return


# 3) 먼지 축적
'''
먼지가 있는 모든 격자에 동시에 5씩 추가
'''
def plus_dust(g):
    for i in range(n):
        for j in range(n):
            if g[i][j] > 0:
                g[i][j] += 5


dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 4) 먼지 확산
'''
꺠끗한 격자에 주변 4방향 격자의 먼지량 합을 10으로 나눈 값만큼 먼지가 확산
동시확산
'''
def PPlus_dust(g):
    new_g = [row[:] for row in g]
    for i in range(n):
        for j in range(n):
            if g[i][j] == 0:
                temp = 0
                for x in range(4):
                    ni, nj = i + dx[x], j + dy[x]
                    if 0<=ni<n and 0<=nj<n:
                        if g[ni][nj] > 0:
                            temp += g[ni][nj]
                new_g[i][j] += temp//10
    return new_g

# 5) 출력
'''
전체 공간의 총 먼지량을 출력한다.
먼지가 있는 곳이 없으면 0을 출력
'''
def print_ans(g):
    ans = 0
    for i in range(n):
        for j in range(n):
            if g[i][j] > 0:
                ans += g[i][j]
    print(ans)


## 메인
for i in range(l):
    # 1) 청소기 이동
    for idx in range(k):
        x, y = clean_unit[idx]
        new_x,new_y = move_unit(g,x,y)
        clean_unit[idx] = [new_x,new_y]

    # 2) 청소
    for idx in range(k):
        x, y = clean_unit[idx]
        clean_dust(g,x,y)

    # 3) 먼지 축적
    plus_dust(g)
    # 4) 먼지 확산
    g = PPlus_dust(g)
    # 5) 출력
    print_ans(g)