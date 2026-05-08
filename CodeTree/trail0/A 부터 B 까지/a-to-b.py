a, b = map(int,input().split())
while a <= b:
    if a > b:
        break
    print(a,end=" ")
    if a % 2 == 0:
        a = a+3
    elif a % 2  != 0:
        a = a*2

