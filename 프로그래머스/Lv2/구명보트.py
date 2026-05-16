people = [70, 50, 80, 50]
limit = 100


def solution(people, limit):
    people.sort(reverse=True)
    start = 0
    end = (len(people) - 1)
    count = 0
    while start <= end:
        if people[start] + people[end] <= limit:
            count += 1
            start += 1
            end -= 1
        elif people[start] + people[end] > limit:
            count += 1
            start += 1
        

    return count


print(solution(people,limit))
