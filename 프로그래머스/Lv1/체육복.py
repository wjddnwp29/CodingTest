'''
체육복은 앞번호나 뒷번호 학생에게만 빌려줄 수 있음
ex 4번이 3번 or 5번
+ 여벌가져온애가 도난당했을 수도 있음.
'''
n = 5
lost = [2,4]
reserve = [1,3,5] # 여벌
arr = [0] * (n)

## 도난당한애들 체크
for i in lost:
    arr[i-1] -= 1


for i in range(n):
    ## (1) 자기가 도난 당했는데 자기꺼있으면 자기한테 +
    if arr[i-1] == -1 and i-1 in reserve:
        arr[i-1] = 0
    ## (2) 자기꺼 있는데 여벌도있다면
    elif arr[i-1] == 0 and i-1 in reserve:
        ## 1번
        if i-1 == 0:
            if arr[i] == -1:
                arr[i] = 0
                reserve.remove(i-1)
        ## 마지막
        elif i-1 == n-1:
            if arr[i-2] == -1:
                arr[i-2] = 0
                reserve.remove(i-1)
        else:
            if arr[i-1] == -1:
                arr[i-1] = 0
                reserve.remove(i-1)
            elif arr[i+1] == -1:
                arr[i+1] = 0
                reserve.remove(i-1)
    
print(arr.count(0))    

def solution(n, lost, reserve):
    arr = [0] * (n)

    ## 도난당한애들 체크
    for i in lost:
        arr[i-1] -= 1

    for i in range(n):
        ## (1) 자기가 도난 당했는데 자기꺼있으면 자기한테 +
        if arr[i-1] == -1 and i-1 in reserve:
            arr[i-1] = 0
            reserve.remove(i-1)
        ## (2) 자기꺼 있는데 여벌도있다면
        elif arr[i-1] == 0 and i-1 in reserve:
            ## 1번
            if i-1 == 0:
                if arr[i] == -1:
                    arr[i] = 0
                    reserve.remove(i-1)
            ## 마지막
            elif i-1 == n-1 and i-1 in reserve:
                if arr[i-2] == -1:
                    arr[i-2] = 0
                    reserve.remove(i-1)
            else:
                if arr[i-1] == -1:
                    arr[i-1] = 0
                    reserve.remove(i-1)
                elif arr[i+1] == -1:
                    arr[i+1] = 0
                    reserve.remove(i-1)
    return arr.count(0)


def solution(n, lost, reserve):
    answer = 0
    ## 자기자신이 도난당하고 여분도 없는 경우
    real_lost = set(lost) - set(reserve) # 진짜 잃어버린애들만남음
    real_reserve = set(reserve) - set(lost) # 진짜 여분있는애들만있음.
    
    for i in sorted(real_reserve):
        if i-1 in real_lost:
            real_lost.remove(i-1)
        elif i+1 in real_lost:
            real_lost.remove(i+1)
    return n-len(real_lost)
    return answer