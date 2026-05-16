def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    s = []

    for i in range(n):
        while s and numbers[s[-1]] < numbers[i]:
            answer[s.pop()] = numbers[i]
        s.append(i)
    return answer



numbers = [9,1,0,3,4]
n = len(numbers)
answer = [-1] * n
s = []

for i in range(n):
    while s and numbers[s[-1]] < numbers[i]:
        answer[s.pop()] = numbers[i]
    s.append(i)
print(answer)

