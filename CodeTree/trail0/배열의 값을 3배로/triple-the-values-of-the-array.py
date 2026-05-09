l = [list(map(int,input().split())) for _ in range(3)]
for _ in range(len(l)):
    for j in range(len(l[0])):
        l[_][j] = l[_][j] * 3

for i in range(3):
    print(*l[i])
