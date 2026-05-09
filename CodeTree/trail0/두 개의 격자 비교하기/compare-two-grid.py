n, m = map(int,input().split())

l = [list(map(int,input().split())) for x in range(n)]
l2 = [list(map(int,input().split())) for x in range(n)]
l3 = [[0]* m for x in range(n)]


for i in range(n):
    for j in range(m):
        if l[i][j] != l2[i][j]:
            l3[i][j] = 1

for i in range(n):
    print(*l3[i])