def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
        return answer
    
    temp = min(arr)
    arr.remove(temp)
    return arr
