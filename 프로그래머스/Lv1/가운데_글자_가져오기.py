def solution(s):
    answer = s
    # 가운데 글자 반환
    ## 홀수
    if len(s) % 2 != 0:
        return answer[(len(s)-1)//2]
    else:
        return answer[(len(s)-1)//2] + answer[(len(s)-1)//2 + 1]

print(solution("abcde"))
print(solution("qwer"))