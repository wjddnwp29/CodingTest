n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
for i in range(n):
    a, b = map(int,input().split())
    t[i] = a
    p[i] = b

ans = [0]

def backtrack(idx,sum):
    if idx > n:
        return
    if idx == n:
        ans[0] = max(ans[0],sum)
        return

    backtrack(idx+t[idx],sum+p[idx])
    backtrack(idx+1,sum)

backtrack(0,0)
print(ans[0])