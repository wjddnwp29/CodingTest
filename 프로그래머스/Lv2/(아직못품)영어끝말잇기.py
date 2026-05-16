def solution(n, words):
    temp = [False for _ in range(len(words)+1)]
    temp[0] = words[0]
    for i in range(1,len(words)):
        ## 아.. 끝말잇기니깐
        if words[i][0] in temp:
            return [len(words) % (n-1)]

        ## 자릿수반환
    ## 0,0 반환
    return answer

'''
1   0
2   1
3   2
'''