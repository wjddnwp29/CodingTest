'''s	answer
"()()"	true
"(())()"	true
")()("	false
"(()("	false
'''
def solution(s):
    answer = s.strip()
    s = []
    for i in answer:
        if i == "(":
            s.append(i)
        else:
            if len(s) != 0:
                s.pop()
            else:
                return False
    if len(s) == 0:
        return True
    else:
        return False

