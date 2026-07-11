n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

vist = [False] * n
ans = float('inf')

def backtrack(idx, depth):
    global ans

    if depth == (n//2):
        a = 0
        b = 0
        for i in range(n):
            for j in range(n):
                if vist[i] == True and vist[j] == True:
                    a += g[i][j]
                elif vist[i] == False and vist[j] == False:
                    b += g[i][j]

        tmp = abs(a-b)
        ans = min(ans,tmp)
        return

    for i in range(idx, n):
        if not vist[i]:
            vist[i] = True
            backtrack(i+1,depth+1)
            vist[i] = False

backtrack(0,0)
print(ans)