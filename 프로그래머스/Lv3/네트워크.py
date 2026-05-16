## A - B - C 

'''
이어진애들 그룹 개수세기
'''

from collections import deque
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
vist = [0] * n

def bfs(index,computers,vist):
    q = deque()
    q.append(index)
    while q:
        index = q.popleft()
        for i in range(n):
            if computers[index][i] == 1 and vist[i] == 0:
                vist[i] = 1
                q.append(i)
    return 1


cnt = 0
for i in range(n):
    if vist[i] == 0:
        vist[i] = 1
        cnt += bfs(i,computers,vist)
print(cnt)