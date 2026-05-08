list = ["apple", "banana", "grape", "blueberry", "orange"]
c = input()
cnt = 0
for word in list:
    if word[2] == c or word[3] == c:
        print(word)
        cnt += 1
print(cnt)