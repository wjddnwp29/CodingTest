def solution(numbers, target):
    def dfs(depth,cur):
        if depth == len(numbers):
            if cur == target:
                return 1
            else:
                return 0
        return dfs(depth+1,cur+numbers[depth]) + dfs(depth+1,cur-numbers[depth])
    return dfs(0,0)

numbers = [1, 1, 1, 1, 1]
target = 3
answer = 0
def dfs(depth,cur):
    if depth == len(numbers):
        if cur == target:
            return 1
        else:
            return 0
    return dfs(depth+1,cur+numbers[depth]) + dfs(depth+1,cur-numbers[depth])
    
    
