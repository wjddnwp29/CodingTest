quiz = ["3 - 4 = -3", "5 + 6 = 11"]

'''
return X, O
'''

answer = []
for i in quiz:
    tmp, ans = i.split("=")
    L, op, R = tmp.split()
    if op == "+":
        result = "O" if int(L) + int(R) == int(ans) else "X"
        answer.append(result)
    elif op == "-":
        result = "O" if int(L) - int(R) == int(ans) else "X" 
        answer.append(result)
print(answer)



def solution(quiz):
    answer = []
    for i in quiz:
        tmp, ans = i.split("=")
        L, op, R = tmp.split()
        if op == "+":
            result = "O" if int(L) + int(R) == int(ans) else "X"
            answer.append(result)
        elif op == "-":
            result = "O" if int(L) - int(R) == int(ans) else "X" 
            answer.append(result)
    return answer