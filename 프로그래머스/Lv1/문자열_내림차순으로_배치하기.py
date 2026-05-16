def solution(s):
    answer = ''.join(sorted(s,reverse = True))
    return answer

'''
65 : A
97 : a'''

s = "Zbcdefg"
answer = ''.join(sorted(s,reverse = True))
print(answer)