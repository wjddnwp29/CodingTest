## result = [3,8] # 3번반복했고 8개의 0이 없어짐
def solution(S):
    Count = 0
    count = 0
    while S != "1":
        Count += 1
        temp = ""
        # 0없애는과정
        for i in S.strip():
            if i == "1":
                temp += i
            else:
                count += 1

        S = str(bin(len(temp))[2::])
    return [Count,count]



