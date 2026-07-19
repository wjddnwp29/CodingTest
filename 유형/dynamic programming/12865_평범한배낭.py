n, k = map(int, input().split())

items = [(0, 0)]

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w, v))

dp = [[0] * (k + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    w, v = items[i]
    for j in range(1, k + 1):
        ## 만약에 배낭에 못 넣는다면...
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            # 배낭에 넣을 수 있다면... 넣은 거랑 안 넣은 거 중 큰 거
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

print(dp[n][k])