'''
land N행 4열

1 - 1행부터 땅을 밟으면 한행씩
2 - 각 행의 4칸 중 한 칸
3 - 같은 열을 연속해서 밟을 수 없다

N이 10^5
N-queen
'''

## 누적합 더하면서 내려오면됨.
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

for i in range(1,len(land)):
    land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
    land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
    land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
    land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

print(max(land[-1]))


def solution(land):
    for i in range(1,len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    return max(land[-1])
