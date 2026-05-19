def apply(s, op, n):
    if op == "+":
        s += n
        if s >= 10000: s -= 10000
    elif op == "-":
        s -= n
        if s < 0: s += 10000
    elif op == "*":
        s *= n
        if s >= 10000: s %= 10000
    return s


def solution(points):
    dp = [False] * 10000
    dp[0] = True
    for a, b in points:
        op1, n1 = a[0], int(a[1:])
        op2, n2 = b[0], int(b[1:])
        
        ndp = [False] * 10000
        for s in range(10000):
            if dp[s]:
                ndp[apply(s,op1,n1)] = True
                ndp[apply(s,op2,n2)] = True
        dp = ndp
    scores = [s for s in range(10000) if dp[s]]
            
    return max(scores), min(scores)
## 2번쨰
def solution(points):
    dp = {0}
    for a, b in points:
        op1, n1 = a[0], a[1::]
        op2, n2 = b[0], b[1::]
        tmp = {}
        for s in dp:
            tmp.add(apply(s,op1,n1))
            tmp.add(apply(s,op2,n2))
        dp = tmp
    return [max(dp),min(dp)]