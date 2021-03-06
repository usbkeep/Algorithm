# https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3


def solution(citations):
    answer = 0
    citations.sort()
    
    length = len(citations)

    for index in range(length):

        if length - index <= citations[index]:
            return length - index

    return answer
