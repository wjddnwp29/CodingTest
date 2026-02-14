#11728 배열 합치기
import sys
N, M = map(int,input().split())
list_num1 = list(map(int,sys.stdin.readline().split()))
list_num2 = list(map(int,sys.stdin.readline().split()))
ans = list_num1 + list_num2
ans.sort()
print(*ans)