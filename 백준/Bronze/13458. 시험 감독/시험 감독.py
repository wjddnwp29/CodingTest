# 총 N 개의 시험장
N = int(input())

'''
각 시험장마다 응시자들이 있따
i번 시험장에 있는 응시자의 수는 Ai명
'''

'''
총감독관 B -> 얘는 시험장에 1명, 한시험장에서 B명만 감시가능
부감독관 C -> 각각의 시험장에 얘는 여러명 있어도됨. , 한시험장에서 C명만 감시가능
'''

list_p = list(map(int,input().split()))
B, C = map(int,input().split())

ans = 0

### (1) 만약에 한 시험장에 B보다 적으면 B만 있으면됨...
### (2) 만약에 B보다 많으면 B한명두고 -> C로 처리하면됨...
#### (2-1) 어떻게?? 나눗셈으로?
### (3) B만큼있으면 B만 있으면됨.. (1)이랑 동일

for i in range(len(list_p)):
    ### 만약 B보다 작거나 같으면...
    if list_p[i] <= B:
        ans += 1
    if list_p[i] > B:
        ans += 1
        p = list_p[i] - B
        ### 여기서 p가 C로 나누어거나 아니거나
        if p % C == 0:
            ans += p // C
        else:
            ans += (p//C) + 1
            
print(ans)
