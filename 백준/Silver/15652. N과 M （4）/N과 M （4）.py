n, m = map(int,input().split())

arr = []

def backtrack(start,k):
    if k == m:
        print(*arr)
        return
    for i in range(start,n+1):
        arr.append(i)
        backtrack(i,k+1)
        arr.pop()
        
backtrack(1,0)
        