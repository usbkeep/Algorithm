# K번째 수
# https://programmers.co.kr/learn/courses/30/lessons/42748

"""
    입출력 예)
        array = [1, 5, 2, 6, 3, 7, 4]
        commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
        return = [5, 6, 3]

	print(solution(array, commands))
"""

def solution(array, commands):
    answer = []

    for low, high, index in commands:
        temp = array[low-1:high]
        temp.sort()
        answer.append(temp[index-1])

    return answer
  
  
