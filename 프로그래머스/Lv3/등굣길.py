def solution(m, n, puddles):
    dp = [[0] * (m+1) for i in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
                
    return dp[n][m]


m = 4
n = 3
puddles = [[2, 2]]

dp = [[0] * (m+1) for i in range(n+1)]
dp[1][1] = 1
for i in range(1, n+1):
    for j in range(1,m+1):
        if i-1 == puddles[0][0] and j-1 == puddles[0][1]:
            dp[i][j] = 0 
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] if j > 0 and i > 0 else 0
print(dp)
