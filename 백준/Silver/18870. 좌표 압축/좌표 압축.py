import sys
input = sys.stdin.readline
n = int(input())

l = list(map(int,input().split()))
l2 = sorted(list(set(l)))

ans = {l2[i] : i for i in range(len(l2))}
for i in l:
    print(ans[i], end = ' ')