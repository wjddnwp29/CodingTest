def solution(number, k):
    stack = []
    for i in number:
        ## 스택에 있고 만약에 k가 0이 아니고 앞에꺼가 뒤에꺼보다 작으면
        while stack and k != 0 and stack[-1] < i:
            stack.pop()
            k-=1
        stack.append(i)


    ## 나머지것들
    if k > 0:
        stack = stack[:-k]
    return "".join(stack)



number = "1924"
k = 2
stack = []
for i in number:
    ## 스택에 있고 만약에 k가 0이 아니고 앞에꺼가 뒤에꺼보다 작으면
    while stack and k != 0 and stack[-1] < i:
        stack.pop()
        k-=1
    stack.append(i)


## 나머지것들
if k > 0:
    stack = stack[:-k]

print("".join(stack))