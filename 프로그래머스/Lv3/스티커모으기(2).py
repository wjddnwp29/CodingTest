sticker = [14, 6, 5, 11, 3, 9, 2, 10]



f = 0
s = 0
for i in range(len(sticker)):
    ## 첫번쨰꺼 뜯는경우
    if i % 2 != 0:
        f += sticker[i]
    else:
        s += sticker[i]
print(max(f,s))