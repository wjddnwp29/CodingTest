# from itertools import combinations

# nums = 	[3, 3, 3, 2, 2, 4]
# result = 3

# ans = []
# for i in combinations(nums,len(nums)//2):
#     ans.append(len(set(i)))
# print(max(ans))

# ## 처음풀이
# def solution(nums):
#     ans = []
#     for i in combinations(nums,len(nums)//2):
#         ans.append(len(set(i)))
#     return max(ans)

## 두번쨰
# def solution(nums):
#     answer = 0
#     nums = [i for i in nums if i not in nums]
#     print(nums)
#     return answer

nums = [3,3,3,2,2,4]
n_set = set(nums)
print(min(len(n_set),len(nums)//2))


