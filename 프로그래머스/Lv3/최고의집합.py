'''
n이 10000 => 백트래킹은 X
두 수의 차이가 작을수록 곱이 커짐
'''
def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    
    answer = [s//n for i in range(n)]
    for i in range(s%n):
        answer[i] += 1
    return answer


s = 13
n = 3
answer = [s//n for i in range(n)]
print(answer)
for i in range(s%n):
        answer[i] += 1
print(answer)




    
        