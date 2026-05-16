def solution(numbers):
    answer = ""
    n = [str(x) for x in numbers]
    n.sort(key = lambda x : x*3 , reverse = True)
    answer = str(int("".join(n)))
    return answer

numbers = [0,0]
answer = ""
n = [str(x) for x in numbers]
n.sort(key = lambda x : x*3 , reverse = True)
answer = str(int("".join(n)))
print(answer)