# 삼각 달팽이
# https://programmers.co.kr/learn/courses/30/lessons/68645

"""
    n = 4
    result = [1,2,9,3,10,8,4,5,6,7]

    print(solution(4))
"""

def solution(n):
    temp = [[0 for col in range(n)] for row in range(n)]

    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):

            if i % 3 == 0:  # 아래
                x += 1
            elif i % 3 == 1:  # 옆
                y += 1
            elif i % 3 == 2:  # 대각
                x -= 1
                y -= 1
            temp[x][y] = num
            num += 1
    print(temp)
    answer = []
    for i in range(n):
        for j in range(i+1):
            answer.append(temp[i][j])
    return answer
