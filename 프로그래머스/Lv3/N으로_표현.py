def solution(N, number):
    dp = [0] * (N+1)
    answer = 0
    return answer

N = 5
number = 12
dp = [set() for i in range(9)]

for i in range(1,9):
    dp[i].add(int(str(N) * (i))) 
    for j in range(0,i):
        for k in dp[j]: # j번 사용하는애
            for l in dp[i-j]: ## i-j번 사용하는애 그래야 두개 더해야 i번
                dp[i].add(k+l)
                dp[i].add(k-l)
                dp[i].add(k*l)
                ## 0인경우 예외처리
                if k != 0 and l != 0:
                    dp[i].add(k//l)
    if number in dp[i]:
        print(i)
        
if number in dp:
    print(-1)
    
def solution(N, number):
    dp = [set() for i in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(N)*(i)))
        for j in range(0,i):
            for k in dp[j]:
                for l in dp[i-j]:
                    dp[i].add(k+l)
                    dp[i].add(k-l)
                    dp[i].add(k*l)
                    if k != 0 and l != 0:
                        dp[i].add(k//l)
        if number in dp[i]:
            return number
    return -1