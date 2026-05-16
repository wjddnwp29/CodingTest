def solution(triangle):
    answer = 0
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        ## 왼쪽끝
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        ## 오른쪽끝
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
            
print(max(triangle[-1]))