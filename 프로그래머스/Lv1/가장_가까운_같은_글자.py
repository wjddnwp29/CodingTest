l = [0 * _ for _ in range(26)]
s = "foobar"
ans = [[0] * _ for _ in range(len(s))]

for i in range(len(s)):
    idx = ord(s[i]) - 97
    if l[idx] == 0:
        l[idx] = i
        ans[i] = -1
    else:
        ans[i] = i-l[idx]
        l[idx] = i

print(ans)


def solution(s):
    l = [-1] * 26
    ans = [0] * len(s)

    for i in range(len(s)):
        idx = ord(s[i]) - ord('a')
        if l[idx] == -1:
            ans[i] = -1
            l[idx] = i
        else:
            ans[i] = i - l[idx]
            l[idx] = i
    return ans

print(solution("foobar"))