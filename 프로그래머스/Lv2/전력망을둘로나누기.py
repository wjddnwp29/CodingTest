def solution(n, wires):
    ans = n
    def dfs(node):
        vist[node] = True
        cnt = 1
        for i in g[node]:
            if not vist[i]:
                cnt += dfs(i)
        return cnt
    
    for i in range(len(wires)):
        g = [[] for _ in range(n+1)]
        vist = [False] * (n+1)
        for idx, (a, b) in enumerate(wires):
            if idx == i:
                continue
            g[a].append(b)
            g[b].append(a)
        cnt = dfs(1)
        ans = min(ans, abs(cnt-(n-cnt)))
    return ans
        
    
        