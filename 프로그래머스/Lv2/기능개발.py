'''
각 기능은 진도가 100%일 떄 서비스 반영가능

뒤에꺼가 앞에보다 먼저될수도있지만
뒤에꺼는 앞에 배포될떄 배포
'''
p = [93,30,55]
s = [1,30,5]
q = []
## 100이고 자기의 위치가 바로 앞이여야함.(그러고 있는거 다 chk 100이 아닐떄까지)

while p:
    ## 업데이트 시키기
    for i in range(len(p)):
        p[i] += s[i]
        
    if p[0] >= 100:
        count = 0
        while p and p[0] >= 100:
            s.pop(0)
            p.pop(0)
            count += 1
        q.append(count)
        
print(q)





