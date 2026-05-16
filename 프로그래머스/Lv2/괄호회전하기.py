s = input().strip()
ans = 0

for i in range(len(s)):
    # 문자열 회전 
    new_s = s[i:] + s[:i]
    
    stack = []
    is_valid = True 
    
    for char in new_s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                is_valid = False
                break
            
            top = stack[-1]
            if (char == ")" and top == "(") or (char == "}" and top == "{") or (char == "]" and top == "["):
                stack.pop()
            else:
                is_valid = False
                break
    if is_valid and len(stack) == 0:
        ans += 1

print(ans)

def solution(s):
    ans = 0

    for i in range(len(s)):
        # 문자열 회전 
        new_s = s[i:] + s[:i]
        
        stack = []
        is_valid = True 
        
        for char in new_s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack:
                    is_valid = False
                    break
                
                top = stack[-1]
                if (char == ")" and top == "(") or (char == "}" and top == "{") or (char == "]" and top == "["):
                    stack.pop()
                else:
                    is_valid = False
                    break
        if is_valid and len(stack) == 0:
            ans += 1
    return ans