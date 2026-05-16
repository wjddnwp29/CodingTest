nums = [1,2,7,6,4]

'''
주어진 숫자 중 3개의 수를 더했을떄 소수가 되는 경우의 개수
'''
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
arr = []
vist = [False] * (len(nums))
cnt = 0
def dfs(nums,arr,idx,vist):
    global cnt
    if len(arr) == 3:
        tmp = sum(arr)
        if is_prime(tmp):
            cnt += 1
        return
    for i in range(idx,len(nums)):
        arr.append(nums[i])
        dfs(nums,arr,i+1,vist)
        arr.pop()
        
dfs(nums,arr,0,vist)
print(cnt)

def solution(nums):
    answer = -1
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    arr = []
    vist = [False] * (len(nums))
    cnt = 0
    def dfs(nums,arr,idx,vist):
        global cnt
        if len(arr) == 3:
            tmp = sum(arr)
            if is_prime(tmp):
                cnt += 1
            return
        for i in range(idx,len(nums)):
            arr.append(nums[i])
            dfs(nums,arr,i+1,vist)
            arr.pop()
    

    return cnt