def solution(n):
    temp = list(str(n).strip())

    temp.sort(reverse = True)
    answer = ''.join(temp)

    return int(answer)

n = 118372
temp = list(str(n).strip())
temp.sort(reverse = True)
answer = ''.join(temp)
print(answer)