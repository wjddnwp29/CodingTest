n = int(input())
l = list(map(int,input().split()))

# 연산자 리스트
s = list(map(int,input().split()))

# 결과들 담을 리스트
ans = []

# 중간 결과를 반영할 변수
tmp = 0

def backtrack(depth, tmp):
    if depth == n:
        ans.append(tmp)
        return

    for i in range(3):
        if s[i] > 0:
            s[i] -= 1
            if i == 0:
                backtrack(depth+1,tmp+l[depth])
            elif i == 1:
                backtrack(depth+1,tmp-l[depth])
            else:
                backtrack(depth+1,tmp*l[depth])
            s[i] += 1




backtrack(1,l[0])
print(min(ans),max(ans))