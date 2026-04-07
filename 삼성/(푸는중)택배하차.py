n, m = map(int,input().split())
# 0) 택배 먼저 넣기
g = [[0] * n for _ in range(n)]

for _ in range(m):
    # 택배번호, 세로크기, 가로크기, 좌측좌표
    k, h, w, c = map(int,input().split())
    temp_r = n-h
    for i in range(0,n):
        for j in range((c-1), (c-1)+w):
            if g[i][j] != 0:
                temp_r = i-h
                break
        if temp_r != n-h:
            break
    for new_row in range(temp_r,temp_r+h):
        for new_col in range((c-1), c-1+w):
            g[new_row][new_col] = k

# 1) 좌측 택배 하차
def left_move(g):
    candidates_left = set()
    for j in range(n):
        left_flag = False
        for i in range(n):
            if g[i][j] != 0:
                candidates_left.add(g[i][j])
                left_flag = True
        if left_flag == True:
            break
    if candidates_left:
        candidates_left = sorted(candidates_left)
        for f in range(n):
            for s in range(n):
                if g[f][s] == candidates_left[0]:
                    g[f][s] = 0

# 3) 우측 택배 하차
def right_move(g):
    candidates_right = set()
    for j in range(n-1,-1,-1):
        right_flag = False
        for i in range(n-1,-1,-1):
            if g[i][j] != 0:
                candidates_right.add(g[i][j])
                right_flag = True
        if right_flag == True:
            break

    if candidates_right:
        candidates_right = sorted(candidates_right)
        for f in range(n):
            for s in range(n):
                if g[f][s] == candidates_right[0]:
                    g[f][s] = 0

# # 2, 4) 떨어짐
# def fall(g):
#
#
#
#
#     return
ans = []
while len(ans) != m:
    # 1) 좌측 택배 하차
    left_move(g)
    if len(ans) == m:
        break
    # 2) 떨어짐
    # fall(g)
    # 3) 우측 택배 하차
    right_move(g)
    if len(ans) == m:
        break
    # # 4) 떨어짐
    # fall(g)

## 답 출력
for ans_i in ans:
    print(ans_i)