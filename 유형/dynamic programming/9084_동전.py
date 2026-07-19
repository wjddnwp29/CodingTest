T = int(input())

for i in range(T):
    c = int(input()) # 몇가지의 케이스
    coins = list(map(int,input().split()))
    n = int(input())

    dp = [0] * (n+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1,n+1):
            if i - coin >= 0:
                dp[i] = dp[i-coin] + 1
print(dp)
