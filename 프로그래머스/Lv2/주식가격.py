def solution(prices):
    answer = [0] * (len(prices))
    s = []
    for i in range(len(prices)):
        while s and prices[s[-1]] > prices[i]:
            j = s.pop()
            answer[j] = i-j
        s.append(i)

    while s:
        j = s.pop()
        answer[j] = (len(prices)-1)-j
    return answer 