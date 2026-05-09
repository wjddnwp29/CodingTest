l = [list(map(int,input().split())) for x in range(3)]
A = input()
l2 = [list(map(int,input().split())) for x in range(3)]
l3 = [[0,0,0] for x in range(3)]

for x in range(len(l)):
    for j in range(len(l[0])):
        l3[x][j] = l[x][j] * l2[x][j]

for i in range(len(l3)):
    print(*l3[i])