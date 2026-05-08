N = int(input())
ans = list(map(int,input().split()))
print(*(x*x for x in ans))