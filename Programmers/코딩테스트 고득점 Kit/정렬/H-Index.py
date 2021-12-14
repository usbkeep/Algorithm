# H-Index
# https://programmers.co.kr/learn/courses/30/lessons/42747

#+ Reference, https://en.wikipedia.org/wiki/H-index
"""
    입출력 예)
        citations = [3, 0, 6, 1, 5]
        return = 3

    print(solution(citations))
"""


def solution(citations):

    answer = 0
    citations.sort()
    
    length = len(citations)

    for index in range(length):

        if length - index <= citations[index]:
            return length - index

    return answer
