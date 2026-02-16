import sys
input = sys.stdin.readline

n, m = map(int,input().split())
l = list(map(int,input().split()))
d = [0] * (n+1)
d[0] = 0
for i in range(1,n+1):
    d[i] = d[i-1] + l[i-1]

for i in range(m):
    a, b = map(int,input().split())
    print(d[b]-d[a-1])