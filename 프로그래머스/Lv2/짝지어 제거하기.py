from collections import deque
s = input().strip()
q = deque()
for i in range(len(s)):
    ## q에 있고 있는거랑 지금들어온게 같을떄
    if q and q[-1] == s[i]:
        q.pop()
    else:
        q.append(s[i])

if len(q) == 0:
    print(1)
else:
    print(0)


def solution(s):
    from collections import deque
    s = s.strip()
    q = deque()
    for i in range(len(s)):
        ## q에 있고 있는거랑 지금들어온게 같을떄
        if q and q[-1] == s[i]:
            q.pop()
        else:
            q.append(s[i])

    if len(q) == 0:
        return 1
    else:
        return 0

