def solution(s):
    s = s.upper()
    c = 0
    for i in s:
        if i == "P":
            c -= 1
        elif i == "Y":
            c += 1
    if c == 0:
        return True
    else:
        return False