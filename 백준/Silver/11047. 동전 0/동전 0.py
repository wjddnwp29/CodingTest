import sys
input = sys.stdin.readline

n, k = map(int,input().split())
l = list(int(input()) for _ in range(n))


# 동전개수
cnt = 0

for i in range(n-1,-1,-1):
    cnt += k // l[i]
    k %= l[i]

print(cnt) 
    