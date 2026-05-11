n, m = map(int, input().split())

# Please write your code here.
def Print(n,m):
    temp = m
    while 1:
        if ((temp % n == 0 and temp % m == 0)):
            print(temp)
            break
        else:
            temp += 1

Print(n,m)