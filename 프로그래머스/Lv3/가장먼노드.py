from collections import deque
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


g = {w:[] for w in range(1,n+1)}

for a,b in vertex:
    g[a].append(b)
    g[b].append(a)
print(g)

vist = set()
dist = [0] * (n+1)

def bfs(start):
    q = deque()
    q.append(start)
    vist.add(start)
    dist[start] = 0
    while q:
        cur = q.popleft()
        for i in g[cur]:
            if i not in vist:
                vist.add(i)
                q.append(i)
                dist[i] = dist[cur] + 1

            
print(bfs(1))

from collections import Counter
c = Counter(dist)
max_dist = max([i for i in c.values()])
print(max_dist)


from collections import deque   
def solution(n, vertex):
    g = {w:[] for w in range(1,n+1)}

    for a,b in vertex:
        g[a].append(b)
        g[b].append(a)


    vist = set()
    dist = [0] * (n+1)

    def bfs(start):
        q = deque()
        q.append(start)
        vist.add(start)
        dist[start] = 0
        while q:
            cur = q.popleft()
            for i in g[cur]:
                if i not in vist:
                    vist.add(i)
                    q.append(i)
                    dist[i] = dist[cur] + 1
    bfs(1)


    from collections import Counter
    c = Counter(dist[1::])
    max_dist = max(c.keys())
    
    return c[max_dist]

    
