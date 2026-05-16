'''
1. 실행 대기 큐에서 대기중인 프로세스 하나를 꺼낸다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면
(방금 꺼낸 프로세스 다시 큐에 넣는다)
3. 만약 그런 프로세스가 없다면 바로 실행
4. 한번실행한건 없앤다.
'''
p = [2,1,3,2]
idx = [i for i in range(len(p))]

    
l = 2 ## idx로 추적해야하는값

flag = -1 # 실행되는 idx값...


# flag가 idx가 아닐떄까지 반복
while flag != l:
    tmp = p.pop(0) ## 실행 대기 큐에서 꺼냄
    tmp_i = idx.pop(0)
    ## 2. 큐에 대기 중인 프로세스 체크
    f = True
    for i in range(len(p)):
        if p[i] > tmp: 
            f = False
            p.append(tmp)
            idx.append(tmp_i)
            break
    if f == True:
        if tmp_i == l:
            print(p[tmp_i])
            break
    
    