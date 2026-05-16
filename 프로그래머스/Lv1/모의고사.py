def solution(answers):
    answer_1 = [1, 2, 3, 4, 5]
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    ans = [0,0,0]
    for idx, answer in enumerate(answers):
        if answer == answer_1[idx%len(answer_1)]:
            ans[0] += 1
        if answer == answer_2[idx%len(answer_2)]:
            ans[1] += 1
        if answer == answer_3[idx%len(answer_3)]:
            ans[2] += 1

    max_score = max(ans)
    ans_2 = []
    for idx,score in enumerate(ans):
        if ans[idx] == max_score:
            ans_2.append(idx+1)
    return ans_2


answer_1 = [1, 2, 3, 4, 5]
answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

answers = [1,2,3,4,5]	
ans = [0,0,0]
for idx, answer in enumerate(answers):
    if answers[idx] == answer_1[idx%len(answer_1)]:
        ans[0] += 1
    elif answers[idx] == answer_2[idx%len(answer_2)]:
        ans[1] += 1
    elif answers[idx] == answer_3[idx%len(answer_3)]:
        ans[1] += 1

max_score = max(ans)
ans_2 = []
for idx,score in enumerate(ans):
    if ans[idx] == max_score:
        ans_2.append(idx+1)
print(ans_2)

    


    