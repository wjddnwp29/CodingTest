def solution(babbling):
    answer = 0
    for i in babbling:
        for word in ["aya","ye","woo","ma"]:
            i = i.replace(word," ")
        if i.strip() == "":
            answer += 1
    return answer
