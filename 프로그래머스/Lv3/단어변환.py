from collections import deque
def solution(begin, target, words):
    answer = 0
    ## 반환할 수 없는 경우.
    if target not in words:
        return 0
    
    ## 하나만 다른지 체크해야함.
    def diff_one(a, b):
        return sum( x!=y for x, y in zip(a,b)) == 1
    
    q = deque()
    q.append([begin,0])
    vist = {begin}
    
    while q:
        cur, step = q.popleft()
        for word in words:
            if word not in vist and diff_one(cur,word):
                if word == target:
                    return step + 1
                vist.add(word)
                q.append([word,step+1])
    
    return answer


def solution(begin, target, words):
    answer = 0
    ## 반환할 수 없는 경우.
    if target not in words:
        return 0
    
    ## 하나만 다른지 체크해야함.
    def diff_one(a, b):
        return sum( x!=y for x, y in zip(a,b)) == 1
    
    a_words = [begin] + words
    g = {w:[] for w in a_words}
    ## 인접 리스트
    for i in range(len(a_words)):
        for j in range(i+1,len(a_words)):
            a, b = a_words[i], a_words[j]
            if diff_one(a,b):
                g[a].append(b)
                g[b].append(a)
                
    
    q = deque()
    q.append([begin,0])
    vist = {begin}
    
    while q:
        cur, step = q.popleft()
        for word in g[cur]:
            if word not in vist:
                if word == target:
                    return step + 1
                vist.add(word)
                q.append([word,step+1])
    
    return answer
