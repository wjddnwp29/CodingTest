N = int(input())


for i in range(1,N+1):
    for j in range(1,N+1):
        if i % 2 != 0:
            print(j,end = "")
        elif i % 2 == 0:
            print(N+1-j,end="")
    print()