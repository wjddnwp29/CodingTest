N = int(input())
temp = 1
sum = 0 
while sum < N:
    sum += temp
    if sum >= N:
        print(temp)
        break
    temp += 1
