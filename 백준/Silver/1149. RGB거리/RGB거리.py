import sys
input = sys.stdin.readline
n = int(input())
c = [[0]*n for _ in range(n+1)]

r = [[0] for _ in range(n+1)]
g = [[0] for _ in range(n+1)]
b = [[0] for _ in range(n+1)]
for i in range(1,n+1):
    r[i],g[i],b[i] = map(int,input().split())
    
c[1][0] = r[1]
c[1][1] = g[1]
c[1][2] = b[1]

for i in range(2, n+1):
    c[i][0] = min(c[i-1][1],c[i-1][2]) + r[i]
    c[i][1] = min(c[i-1][2],c[i-1][0]) + g[i]
    c[i][2] = min(c[i-1][1],c[i-1][0]) + b[i]
    
print(min(c[n][0], c[n][1], c[n][2]))