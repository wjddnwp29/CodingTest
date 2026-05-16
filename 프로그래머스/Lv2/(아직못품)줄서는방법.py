n, k = map(int,input().split())
s = []
vist = [0] * (n+1)
answer = []
def backtrack(start):
    if start == n:
        print(s)
        answer.append(s)
        return
    for i in range(1, n+1):
        if vist[i] == 0:
            vist[i] = 1
            s.append(i)
            backtrack(start+1)
            s.pop()
            vist[i] = 0

print(backtrack(0))
print(answer)


import math

def solution(n, k):
    answer = []
    l = []
    k = k-1
    for n in range(1,n+1) :
        l.append(n)
    
    while l :
        a = k // math.factorial(n-1)
        answer.append(l[a])
        del l[a]
        
        k = k % math.factorial(n-1)
        n -= 1
        
    return answer

print(solution(3,5))