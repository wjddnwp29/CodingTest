n, m = map(int,input().split())
l = list(map(int,input().split()))
l.sort()

arr = []
def backtrack(k):
    if k == m:
        print(*arr)
        return
    for i in l:
        if i not in arr:
            arr.append(i)
            backtrack(k+1)
            arr.pop()

backtrack(0)