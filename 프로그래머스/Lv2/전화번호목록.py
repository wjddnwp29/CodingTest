l = ["119", "97674223", "1195524421"]

# ## 첫번쨰풀이
# flag = True
# for i in range(len(l)):
#     length = len(l[i])
#     for j in range(i+1,len(l)):
#         if i == j:
#             continue
#         if length <= len(l[j]):
#             if l[i] == l[j][:length]:
#                 flag = False
#                 break

# print(flag)  


# 두번쨰 풀이
l.sort()
print(l)
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        length = len(phone_book[i])
        if phone_book[i] == phone_book[i+1][:length]:
            return False
    return True