'''
N+1일째 되는날 퇴사 
N일동안 최대한 많은 상담
하루에 하나씩 서로 다른 상담
T : 걸리는 기간 , P : 금액
'''

n = int(input())
g = [list(map(int,input().split())) for _ in range(n)]

answer = [0]
def backtrack(day,money):
    if day > n:
        return
    if day == n:
        answer[0] = max(answer[0],money)
        return
    
    backtrack(day+g[day][0],money+g[day][1])
    backtrack(day+1,money)
backtrack(0,0)
print(answer[0])