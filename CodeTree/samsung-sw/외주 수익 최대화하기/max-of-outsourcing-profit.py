n = int(input())

l_t = []
l_p = []

for i in range(n):
    t, p = map(int,input().split())
    l_t.append(t)
    l_p.append(p)

ans = 0

def backtrack(day,money):
    global ans
    if day == n:
        ans = max(ans,money)
        return
    backtrack(day+1,money)
    if day + l_t[day] <= n:
        backtrack(day+l_t[day],money+l_p[day])


backtrack(0,0)
print(ans)