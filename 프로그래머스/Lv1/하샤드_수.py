def solution(x):
    temp = list(str(x).strip())
    temp = list(map(int,temp))

    temp_sum = sum(temp)

    if x % temp_sum == 0:
        return True
    else:
        return False

x = 10
temp = list(str(x).strip())
temp = list(map(int,temp))

temp_sum = sum(temp)

if x % temp_sum == 0:
    return True
else:
    return False