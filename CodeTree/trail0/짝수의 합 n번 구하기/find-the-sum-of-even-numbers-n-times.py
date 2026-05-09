N = int(input())


for i in range(N):
    x, y = map(int,input().split())
    temp = 0
    for j in range(x,y+1):
        if j % 2 == 0:
            temp += j
    print(temp)