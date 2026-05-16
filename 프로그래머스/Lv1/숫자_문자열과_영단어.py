def solution(s):
    num_dict = {'zero':'0', 'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}            

    for i,j in num_dict.items():
        s = s.replace(i,j)

    return s

# 숫자	영단어
# 0	zero
# 1	one
# 2	two
# 3	three
# 4	four
# 5	five
# 6	six
# 7	seven
# 8	eight
# 9	nine

s = "one4seveneight"
num_dict = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}            

for i,j in num_dict.items():
    s = s.replace(i,j)



