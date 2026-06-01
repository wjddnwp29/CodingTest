# 콜라 빈 병 2개를 가져다 주면 콜라 1병을 줌
# 빈 병 20개를 가져다주면 몇 병을 받을 수 있는가
# 보유중인 빈 병이 2개 미만이면 콜라를 받을 수 없음

def solution(a, b, n):
    answer = 0
    while a <= n:
        n -= a
        answer += b
        n += b
    return answer

print(solution(2,1,20))

# a개를 가져다주면 b개를 줌 
# n개를 가져가면 몇병을 받을수있을까?
# 단 보유중인개 a개 미만이면 추가적인 빈 병은 받을 수 X

a,b,n = 2,1,20

# a개 미만일동안
cnt = 0
while a < n:
    n -= a # a개를 줬기떄문에
    cnt += b # b개를 더함.
    n += b # b개를 받음.
    
    