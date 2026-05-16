def solution(n):
    temp = list(str(n).strip())[::-1]
    answer = [0] * (len(temp))

    for i in range(0,len(temp)):
        answer[i] = int(temp[i])

    return answer


def solution(n):
    arr = list(str(n))
    arr.reverse()
    answer = list(map(int,arr))
    print(answer)