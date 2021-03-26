# https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3


def solution(array, commands):
    answer = []

    for low, high, index in commands:
        temp = array[low-1:high]
        temp.sort()
        answer.append(temp[index-1])

    return answer
  
  
