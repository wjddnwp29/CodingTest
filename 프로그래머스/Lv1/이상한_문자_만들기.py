## 각 단어의 짝수번쨰는 대문자 / 홀수번째는 소문자
def solution(s):
    answer = ''
    return answer


# s = "try hello world"
# blank = []
# ## 공백을 저장해놔야함.
# for i in s:
    

# temp = s.split()
# for i in range(len(temp)):
#     t = ""
#     for j in range(len(temp[i])):
#         if j % 2 == 0:
#             t += temp[i][j].upper()
#         else:
#             t += temp[i][j].lower()
#     temp[i] = t

s = "try hello world"
ans = ""
idx = 0
for i in s:
    # 공백일떄
    if i == " ":
        ans += " "
        idx = 0
    ## 공백이 아닐때
    else:
        if idx % 2 == 0:
            ans += i.upper()
        else:
            ans += i.lower()
        idx += 1
print(ans)





