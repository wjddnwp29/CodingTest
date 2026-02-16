import sys
input = sys.stdin.readline

s = input().strip()
c = input().strip()

cnt = 0
pos = 0

while True:
    pos = s.find(c, pos)
    
    if pos == -1: 
        break
        
    cnt += 1
    pos += len(c) 

print(cnt)