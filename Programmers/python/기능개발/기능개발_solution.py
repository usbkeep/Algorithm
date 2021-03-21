def solution(progresses, speeds):

    answer = []
    time = 1
    complete = 0

    while len(progresses) > 0:
        temp = progresses[0] + (speeds[0] * time)

        if temp >= 100:
            progresses.pop(0)
            speeds.pop(0)
            complete += 1
        else:
            if complete > 0:
                answer.append(complete)
                complete = 0
            time += 1
    answer.append(complete)
    return answer
