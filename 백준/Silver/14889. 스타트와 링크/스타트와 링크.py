n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]


ans = [1e9]
'''
n 명 -> 각각
1->2 나머지... 
3 -> 4 나머지는 자연스럽게 결정이난다. 그러면?
'''

v = [False] * n
def backtrack(i,cnt):
    if cnt == n//2:
        s_score=0
        l_score=0
        for i in range(n):
            for j in range(n):
                if v[i] == True and v[j] == True:
                    s_score += g[i][j]
                elif v[i] == False and v[j] == False:
                    l_score += g[i][j]
        ans[0] = min(ans[0], abs(s_score-l_score))
        
    for i in range(i,n):
        if not v[i]:
            v[i] = True
            backtrack(i+1,cnt+1)
            v[i] = False

backtrack(0,0)
print(ans[0])