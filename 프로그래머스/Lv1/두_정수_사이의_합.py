def solution(a, b):
    temp = 0
    if a == b:
        temp = a
    elif a > b:
        for i in range(b,a+1):
            temp += i
    elif a < b:
        for i in range(a,b+1):
            temp += i
    return temp


print(solution(5,3))
print(solution(0,0))
print(solution(3,5))


def solution(a, b):
    return sum(range(min(a,b), max(a,b) + 1))



# 등차수열의 합
'''
(a+b) * (abs(a-b) + 1) // 2
'''
def solution(a,b):
    return ((a+b) * (abs(a-b) + 1)) // 2