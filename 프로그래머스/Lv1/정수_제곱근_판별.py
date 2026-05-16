def solution(n):

    temp = n ** (0.5)

    if temp % 1 == 0:
        return (temp+1) ** 2
    else:
        return -1



n = 121
temp = math.sqrt(n)
# if type(temp) == "int":
#     return (n+1) ** 2
print(temp)


n = 121
temp = math.sqrt(n)
float_n = float(n)
print(temp*temp)
print(float_n*float_n)
