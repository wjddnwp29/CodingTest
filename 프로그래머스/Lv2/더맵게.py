s = [1, 2, 3, 9, 10, 12]
K = 7

# '''
# 모든 음식의 스코빌 지수 K 이상될떄까지의 cnt 반환
# '''
# cnt = 0
# while 1:
#     s.sort()
#     l = len(s)
#     ## 모든 음식의 스코빌 지수 체크
#     flag = 0
#     for i in s:
#         if i >= K:
#             flag += 1
#     if flag == l:
#         break
#     else:
#         s[1] = s[0] + (s[1]*2)
#         s.pop(0)
#         cnt += 1
# print(cnt)
    
        
# def solution(s, K):
#     cnt = 0
#     while 1:
#         s.sort()
#         l = len(s)
#         ## 모든 음식의 스코빌 지수 체크
#         flag = 0
#         for i in s:
#             if i >= K:
#                 flag += 1
#         if flag == l:
#             break
#         else:
#             s[1] = s[0] + (s[1]*2)
#             s.pop(0)
#             cnt += 1
#     return cnt

def solution(scoville, K):
    import heapq
    heapq.heapify(s)  
    print(s)

    cnt = 0

    while s[0] < K:
        if len(s) < 2:
            return -1
        a = heapq.heappop(s)
        b = heapq.heappop(s)
        heapq.heappush(a+b**2)
        cnt += 1
    return cnt
# import heapq
# heapq.heapify(s)  
# print(s)

# cnt = 0

# while s[0] < K:
#     if len(s) < 2:
#         return -1
#     a = heapq.heappop(s)
#     b = heapq.heappop(s)
#     heapq.heappush(a+b**2)
#     cnt += 1

    