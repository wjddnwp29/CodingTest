tmp_3 = 0
tmp_5 = 0
for i in range(10):
    num = int(input())
    if num % 3 == 0:
        tmp_3 += 1
    if num %5 == 0:
        tmp_5 += 1

print(tmp_3, tmp_5)