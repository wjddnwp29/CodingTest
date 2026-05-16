"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"

def solution(s):
    answer = list(map(int,s.split()))
    answer = str(min(answer)) + " " + str(max(answer))
    return answer

print(solution("1 2 3 4"))