l = [list(map(int,input().split())) for x in range(4)]

temp = 0
for i in range(len(l)):
    for j in range(i+1):
        temp += l[i][j]
print(temp)