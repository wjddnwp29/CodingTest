def solution(money):
    answer = []
    a = money // 5500
    if a > 0:
        answer.append(a)
        answer.append(money - (5500*a)) 
    return answer


print(solution(5500))
print(solution(15000))
