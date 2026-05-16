def solution(n):
    start = 1
    end = 1
    count = 0
    while start <= n and end <= n:
        temp = 0
        for i in range(start,end+1):
            temp += i
        
        if temp == n:
            count += 1
            end += 1

        elif temp < n:
            end += 1
            
        else:
            start += 1
    return count
print(solution(15))



    
    


