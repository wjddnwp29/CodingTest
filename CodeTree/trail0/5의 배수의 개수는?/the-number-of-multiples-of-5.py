l = [list(map(int,input().split())) for x in range(4)]

cnt = 0

for i in l:
    for j in i:
        if j % 5 == 0:
            cnt += 1
print(cnt)