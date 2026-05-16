""
[1,1,3,3,0,1,1]	
[1,3,0,1]
""

def solution(arr):
    answer = []
    cur = arr[0]
    answer.append(cur)
    for i in range(1,len(arr)):
        if cur == arr[i]:
            continue
        else:
            cur = arr[i]
            answer.append(cur)

    return answer

