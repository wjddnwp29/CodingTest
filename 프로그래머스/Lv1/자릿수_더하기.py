def solution(n):
    answer = 0
    temp = str(n).strip()
    for i in temp:
        answer += int(i)

    return answer