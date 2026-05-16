'''
1. 속한 노래가 많이 재생된 장르를 먼저 수록함.
2. 장르 내에서 많이 재생된 노래를 먼저 수록함.
3. 장르 내에서 재생횟수가 같은 노래 중에서는 고유 번호가 낮은(앞에있는)애를 먼저 수록함.


## 베스트앨범에는 장르에 속한애들 2개씪 oo
## 1개라면 1개만 넣으면됨.
'''
g = ["classic", "pop", "classic", "classic", "pop"]
p = [500, 600, 150, 800, 2500]
d = {}
t = {}

for i in range(len(g)):
    if g[i] not in d:
        d[g[i]] = []
        t[g[i]] = 0
    d[g[i]].append((p[i],i))
    t[g[i]] += p[i]

## 재생수기준으로 정렬
t = dict(sorted(t.items(), key=lambda x:x[1], reverse=True))

## 이제 여기서 길이만큼해서 장르별로 뽑으면됨
## 이제 장르내에서 많이 재생된 순으로 정렬, 고유번호가 낮은 애들 먼저수록
for g in d:
    d[g] = sorted(d[g], key=lambda x : (-x[0],x[1]))
print(d)
ans = []

for i in t.keys():
    for p,index in d[i][:2]:
        ans.append(index)
        
print(ans)



