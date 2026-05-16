def solution(n):
    start = 1
    while n % start != 1:
        start += 1
    
    return start

print(solution(10))
print(solution(12))