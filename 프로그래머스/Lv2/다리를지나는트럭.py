'''
정해진 순서대로 다리 건넘.
ans : 모든 트럭이 다리를 건너려면 최소 몇초가 걸리냐?
bridge_length = 다리에 올라갈 수 있는 트럭 수
weight = 다리가 견딜수있는 최대 무게(완전히 오르지 않은건 무시)
'''


l = 2 # 다리에 올라갈 수 있는 트럭 수
w = 10 # 다리가 최대 견딜 수 있는 무게
## 위의 두가지 만족해야함.
t = [7,4,5,6]
ans = 0 # 걸리는 시간
## 무조건 l만큼의 시간이 지나면 pop 되는게 사실.
## ans % l == 0: ??? 1이면 계속 왼쪽으로 pop됨

from collections import deque

cur_bridge = deque([0] * l) # 현재 다리에 올라가있는애들
cur_weight = 0 # 다리에 올라가있는애 무게

while t: 
    cur_weight -= cur_bridge.popleft() # 앞에꺼뺴줘야함.
    if cur_weight + t[0] <= w:
        tmp = t.pop(0)
        cur_bridge.append(tmp)
        cur_weight += tmp
    else:
        cur_bridge.append(0)
    ans += 1

ans += l
print(ans)    




