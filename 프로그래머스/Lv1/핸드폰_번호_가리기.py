def solution(phone_number):
    s = len(phone_number)-4
    answer = (s*"*") + phone_number[s::]
    print(answer)
    return answer

phone_number = "01033334444"
s = len(phone_number)-4
answer = (s*"*") + phone_number[s::]
print(answer)
