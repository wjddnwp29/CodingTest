def solution(array, commands):
    answer = [0] * len(commands)
    # 명령만큼 바복해야함.
    for i in range(len(commands)):
        temp = array[commands[i][0]-1:commands[i][1]]
        temp.sort()
        answer[i] = temp[commands[i][2]-1]

    return answer


