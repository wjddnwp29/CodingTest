def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    answer = sum(A*B for A,B in zip(A,B))

    return answer



