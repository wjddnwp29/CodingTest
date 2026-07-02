'''
1
1
2 2
'''

# 식당의 수
n = int(input())

# 각 식당에 있는 고객의 수
c_list = list(map(int,input().split()))

# 검사팀장이 검사할 수 있는 최대 고객 수와 검사팀원이 검사할 수 있는 최대 고객 수
chk_list = list(map(int,input().split()))

# 최소의 수(답)
ans = n

## 한번 돌면서 검사팀장만큼 빼야함.
for i in range(n):
    temp = c_list[i] - chk_list[0]
    if temp > 0:
        c_list[i] = temp
    else:
        c_list[i] = 0


## 이제 두번돌면서 검사팀원으로 체크
for i in range(n):
    if c_list[i] != 0:
        temp1 = c_list[i] // chk_list[1]
        temp2 = c_list[i] % chk_list[1]
        ans += temp1
        if temp2 != 0:
            ans += 1
print(ans)

