N = int(input())


for i in range(1,N+1):
    for j in range(1,N+1):
        if j % 2 != 0:
            print(i,end="")
        elif j % 2 == 0:
            print(N+1-i,end="")
    print()
