start, end = map(int, input().split())

# Please write your code here.
## 약수의 개수가 3개인 애들
cnt = 0

for i in range(start,end+1):
    temp  = 0
    for j in range(1,i+1):
        if i % j == 0:
            temp += 1
    if temp == 3:
        cnt += 1
print(cnt)