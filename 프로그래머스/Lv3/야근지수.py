'''
야근지수 : 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값
1시간동안 작업량 1만큼을 처리할 수 있다.
'''


def solution(n, works):
    works = [-w for w in works]
    heapq.heapify(works)

    # n이 0이아닐떄랑, sum(works)가 0일 아닐떄까지
    while n > 0 and works[0] < 0:
        tmp = heapq.heappop(works)
        heapq.heappush(works,tmp+1)
        n -= 1

    answer = 0
    for i in works:
        answer = answer + i**2
    
    return answer

'''
n - 퇴근까지 남은 시간
works - 각 일에 대한 작업량
'''
'''
전체적인 평균 => 하나줄면 X
계속 정렬? ==> O(n) 2 * 10^5 * 10^7 = 10^12 X
큰값을 하나씩 뺴서 줄이면
'''

import heapq

n = 4
works = [4,3,3]
works = [-w for w in works]
heapq.heapify(works)

# n이 0이아닐떄랑, sum(works)가 0일 아닐떄까지
while n > 0 and works[0] < 0:
    tmp = heapq.heappop(works)
    heapq.heappush(works,tmp+1)
    n -= 1

ans = 0
for i in works:
    ans = ans + i**2
print(ans)
