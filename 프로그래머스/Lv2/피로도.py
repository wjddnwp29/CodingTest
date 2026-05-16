def solution(k, dungeons):
    answer = -1
    n = len(dungeons)
    vist = [False] * n
    
    def dfs(cur_k, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        for i in range(n):
            if not vist[i] and cur_k >= dungeons[i][0]:
                vist[i] = True
                dfs(cur_k - dungeons[i][1], cnt+1)
                vist[i] = False
    dfs(k,0)
    return answer