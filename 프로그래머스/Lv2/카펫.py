def solution(brown, yellow):
    s = brown + yellow
    for x in range(1, s+1):
        if s % x == 0:
            y = s // x
            if x >= y:
                if 2*(x+y) - 4 == brown:
                    return [x,y]

