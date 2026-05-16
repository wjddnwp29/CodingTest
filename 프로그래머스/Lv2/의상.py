clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
d = {}
for i,j in clothes:
    if j not in d:
        d[j] = 0
    d[j] += 1
ans = 1
for i in d.values():
    ans *= (i+1)
print(ans-1)