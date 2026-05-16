c = [3, 0, 6, 1, 5]
#### h = 3 ==> 인용된 논문 h번이상 h편 이상/// 나머지논문은 h번이하 
#### h의 최대값이 answer
c.sort()
answer = 0
for i in range(len(c)):
    # 자기보다 뒤에서 인용된 논문 개수
    cnt_b = len(c[i::])
    # 자기보다 앞에있는애들 다 더한 값
    cnt_p = len(c[:i+1])

    ## 자기보다 뒤에서 인용된 논문 횟수가 h편 이상이라면...
    ## 자기보다 앞에있는애들 다 더한게 h번 보다 작다면....
    if  (cnt_b >= c[i]) and (cnt_p <= c[i]):
        answer = c[i]
print(c[i])

def solution(citations):
    citations.sort() # [0, 1, 3, 5, 6]
    n = len(citations)
    
    for i in range(n):
        # h_candidate: 현재 논문(i번째)을 포함하여 나보다 많이 인용된 논문의 총 개수
        h_candidate = n - i 
        
        # 만약 현재 논문의 인용 횟수가 이 '개수'보다 크거나 같다면?
        # 그게 바로 h-index의 정의를 충족하는 순간!
        if citations[i] >= h_candidate:
            return h_candidate
            
    return 0
print(solution(c))
    

