a, b = map(int,input().split())
dp = [0] * 10
dp[0] = a
dp[1] = b
for i in range(2,10):
    dp[i] = dp[i-2] + dp[i-1]
    if dp[i] >= 10:
        dp[i] = dp[i] % 10

print(*dp)
