from itertools import combinations
grid = [[1,0,1,1],[0,1,0,0],[1,1,0,0],[0,0,1,1],[0,1,1,1]]
## 풀이1
def solution(grid):
    n, m = len(grid), len(grid[0])
    mask_all = (1 << m) - 1
    masks = [sum(1 << j for j in range(m) if grid[i][j]) for i in range(n)]
    for cnt in range(n + 1):                  # 0개부터 n개까지
        for combo in combinations(range(n), cnt):
            tmp = 0
            for k in combo:
                tmp |= masks[k]
            if tmp == mask_all:
                return [k + 1 for k in combo]
    return []

## 풀이2
def solution(grid):
    n, m = len(grid), len(grid[0])
    ans = (1<<m) - 1
    masks = []
    for i in range(n):
        mask = 0
        for j in range(m):
            if grid[i][j]:
                mask += 1 << j
        masks.append(mask)
    
    best = None
    def backtrack(idx,cur,chosen):
        nonlocal best
        
        if cur == ans:
            tmp = (len(chosen), list(chosen))
            if best is None or tmp < best:
                best = tmp
            return
        
        if idx == n:
            return
        ## idx 문제 고르는 경우
        chosen.append(idx+1)
        backtrack(idx+1,cur | masks[idx], chosen)
        chosen.pop()
        ## idx 문제 안고르는 경우
        backtrack(idx+1, cur, chosen)
    
    backtrack(0, 0, [])
    return best[1] if best else []