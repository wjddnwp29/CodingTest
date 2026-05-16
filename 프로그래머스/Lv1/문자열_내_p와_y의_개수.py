def solution(s):
    s=s.upper()
    temp = 0
    for i in s:
        if i == "P":
            temp += 1
        elif i == "Y":
            temp -= 1
    if temp == 0:
        return True
    else:
        return False



s = "pPoooyY"
s=s.upper()
temp = 0
for i in s:
    if i == "P":
        temp += 1
    elif i == "Y":
        temp -= 1
if temp == 0:
    return True
else:
    return False


return s.upper().count("P") == s.upper().count("Y":)