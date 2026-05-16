def solution(sizes):
    answer = 0
    return answer


'''
일단은 먼저 모든 명함 직사각형 크기 구해야함.
'''

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
h = []
w = []

for i,j in sizes:
    h.append(max(i,j))
    w.append(min(i,j))
    
print(max(h)*max(w))