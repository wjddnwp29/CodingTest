def solution(operations):
    l = []
    for i in operations:
        a, b = i.split()
        num = int(b)
        
        if a == "I":
            heappush(l,num)
        else:
            if l:
                if num == 1:
                    tmp = max(l)
                    l.remove(tmp)
                else:
                    heappop(l)

    if len(l) == 0:
        answer = [0,0]
    else:
        answer = [max(l), heappop(l)]
    return answer

from heapq import heappop, heappush
op = ["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]
answer = []
l = []
for i in op:
    a, b = i.split()
    num = int(b)
    
    if a == "I":
        heappush(l,num)
    else:
        if l:
            if num == 1:
                tmp = max(l)
                l.remove(tmp)
            else:
                heappop(l)

if len(l) == 0:
    answer = [0,0]
else:
    answer = [max(l), heappop(l)]
    
    
from heapq import heappop, heappush
## min, max로 관리하는 풀이
def solution(operations):
    answer = []
    max_h = []
    min_h = []
    
    vist = [False] * (len(operations))
    
    for i, s in enumerate(operations):
        op, num = s.split()
        num = int(num)
        
        if op == "I":
            heappush(max_h,(-num,i))
            heappush(min_h,(num,i))
            vist[i] = True
        else:
            if num == 1:
                while max_h and not vist[max_h[0][1]]:
                    heappop(max_h)
                if max_h:
                    vist[max_h[0][1]] = False
                    heappop(max_h)
            else:
                while min_h and not vist[min_h[0][1]]:
                    heappop(min_h)
                if min_h:
                    vist[min_h[0][1]] = False
                    heappop(min_h)
    while max_h and not vist[max_h[0][1]]:
        heappop(max_h) 
    while min_h and not vist[min_h[0][1]]:
        heappop(min_h)     
        
    if not max_h or not min_h:
        return [0,0]
    
            
    return [-max_h[0][0], min_h[0][0]]
    
    
    