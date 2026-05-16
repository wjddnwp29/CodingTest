def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if i != j:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer