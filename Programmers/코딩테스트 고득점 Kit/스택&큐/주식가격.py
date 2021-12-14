# 주식가격
# https://programmers.co.kr/learn/courses/30/lessons/42584

"""
    입출력 예)
        prices = [1, 2, 3, 2, 3]
        return = [4, 3, 1, 1, 0]

    print(solution(prices))
"""


def solution(prices):

    answer = [0] * len(prices)
    stack = []

    for index, p in enumerate(prices):

        while stack and prices[stack[-1]] > p:
            temp = stack.pop()
            answer[temp] = index - temp
        stack.append(index)

    for s in stack:
        answer[s] = len(prices)-1 - s

    return answer
