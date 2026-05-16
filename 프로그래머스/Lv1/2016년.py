def solution(a, b):
    answer = 0
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    temp = sum(day[:a-1]) + b
    answer = (temp + 4) % 7   

    if answer == 1:return "MON"
    elif answer == 2:return "TUE"
    elif answer == 3:return "WED"
    elif answer == 4:return "THU"
    elif answer == 5:return "FRI"
    elif answer == 6:return "SAT"
    else:return "SUN"
    

print(solution(5,24))

'''
1월1일이 금요일 ==> 
월요일 1
화 2
수 3
목 4
금 5
토 6
일 7


[31,29,30,30,31,30,31,31,30,31,30,31]
==> 이렇게하고....

요일 체크해줘야하는게 (i+1) % 7


'''
day = [31,29,31,30,31,30,31,31,30,31,30,31]
print(sum(day))