def solution(participant, completion):
    answer = 0
    temp = {}
    for p in participant:
        h = hash(p)
        temp[h] = p
        answer += hash(p)
        
    for c in completion:
        answer -= hash(c)

    return temp[answer]