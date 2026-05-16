from itertools import permutations
def solution(numbers):
    answer = 0
    return answer


numbers = [1,7]
ans = set()

## 앞으로 탐색


## 뒤로 탐색 흐음...아닌듯 첫번쨰 마지막꺼 이렇게 될수도있음. 그럼 백트래킹? ==> 이래버림녀 13 은되는데 31? ㅇㅇ 됨 # 하나만 뽑힐수도있잖아 그러면 애매 조합?


for i in range(len(numbers)):
    for j in permutations(numbers,i+1):
        temp = "".join(map(str,j))
        ans.add(int(temp))


cnt = 0
for i in ans:
    temp = 0
    for j in range(1,i+1):
        if i % j == 0:
            temp += 1
    if temp == 2:
        cnt += 1
print(cnt)    

from itertools import permutations
def solution(numbers):
    ans = set()
    for i in range(len(numbers)):
        for j in permutations(numbers,i+1):
            temp = "".join(map(str,j))
            ans.add(int(temp))
    cnt = 0
    for i in ans:
        if i < 2:
            continue
        temp = True
        for j in range(2,int(i**0.5)+1):
            if i % j == 0:
                temp = False
        if temp == True:
            cnt += 1
    return cnt