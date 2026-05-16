# word_list = ["A","E","I","O","U"]
# temp = []
# ans = 0

# def backtrack(word):
#     global ans
#     if len(temp) == 5:
#         return
#     for i in word_list:
#         temp.append(i)
#         ans += 1
#         if "".join(temp) == word:
#             return
#         backtrack(word)
#         temp.pop()

# def solution(word):
#     backtrack(word)
#     return ans


word_list = ["A","E","I","O","U"]
target = "AAAAE"

arr = []
cnt = 0
flag = False
def dfs(depth):
    global cnt, flag
    if flag == True or depth  == 5:
        return
    
    for i in range(len(word_list)):
        cnt += 1
        arr.append(word_list[i])
        if target == "".join(arr):
            flag = True
            return
        dfs(depth+1)
        if flag == True:
            return
        arr.pop()
dfs(0)  
print(cnt)

# word_list = ["A","E","I","O","U"]
# target = "AAAAE"
# arr = []
# cnt = 0
# found = False

# def dfs(depth):
#     global cnt, found
#     if found or depth == 5:
#         return
#     for i in range(len(word_list)):
#         cnt += 1
#         arr.append(word_list[i])
#         if target == "".join(arr):
#             found = True
#             return
#         dfs(depth+1)
#         if found:  # 찾았으면 pop 없이 바로 return
#             return
#         arr.pop()

# dfs(0)
# print(cnt)  # 6