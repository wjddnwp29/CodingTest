a, b = map(int, input().split())

# Please write your code here.
### 3,6,9 가 들어있는지 체크
### 그 수 자체가 3의 배수인지를 체크
def chk_369(num):
    for a in str(num):
        if int(a) in [3,6,9]:
                return True
    return False
         
def chk_3(num):
    if num % 3 == 0:
        return True
    else:
        return False


cnt = 0
for i in range(a,b+1):
    if chk_369(i) or chk_3(i):
        cnt += 1
print(cnt)