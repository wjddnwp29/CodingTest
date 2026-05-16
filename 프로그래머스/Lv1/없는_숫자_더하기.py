def solution(numbers):
    # 0부터 9까지의 수 19 28 37 46 
    answer = 45
    for i in numbers:
        answer -= i
    return answer