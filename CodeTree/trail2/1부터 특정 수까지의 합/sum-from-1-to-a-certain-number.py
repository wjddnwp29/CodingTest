n = int(input())

# Please write your code here.


def ans(n):
    temp = 0
    for i in range(1,n+1):
        temp += i
    return temp // 10
print(ans(n))