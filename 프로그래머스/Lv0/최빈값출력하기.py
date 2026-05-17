def solution(array):
    answer = 0
    return answer
array = [1, 2, 2, 3, 3, 4]
from collections import Counter
c = Counter(array)
m = max(c.values())
l = [k for k,v in c.items() if v == m]
print(l)


print(c.items())
if len(l) > 2:
    print(-1)
else:
    print(l[0])