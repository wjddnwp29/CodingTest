n = int(input())

# Please write your code here.
def ans(n):
    s = 0
    for i in str(n).strip():
        s += int(i)

    if s % 5 == 0 and n % 2 == 0:
        return "Yes"
    else:
        return "No"
print(ans(n))