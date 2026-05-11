n = int(input())

# Please write your code here.
temp = 1
for i in range(n):
    for j in range(n):
        if temp == 9:
            print(temp, end=" ")
            temp = 1
        else:
            print(temp, end = " ")
            temp += 1
    print()