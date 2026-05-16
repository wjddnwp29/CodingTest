word_list = ["A","E","I","O","U"]
temp = []
global ans_cnt
ans_cnt = 0

def backtrack(n,word):
    if n == 5:
        ans = "".join(temp)
        ans_cnt+=1
        if word == ans:
            print(ans_cnt)
            return
        else: 
            return
        
    for i in word_list:
        temp.append(i)
        backtrack(n+1,word)
        temp.pop()

backtrack(0,"AAAAA")
