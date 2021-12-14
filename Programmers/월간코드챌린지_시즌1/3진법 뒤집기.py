# 3진법 뒤집기
# https://programmers.co.kr/learn/courses/30/lessons/68935

"""
    n = 45
    result = 7

    print(solution(45))
"""


def solution(n):

    temp = base10_to_base3(n)
    answer = base3_to_base10(temp)

    return answer


def base3_to_base10(stack):
    result = 0
    i = 1
    while stack:
        result += stack.pop() * i
        i *= 3

    return result


def base10_to_base3(n):
    stack = []
    quotient = 1
    while quotient:

        quotient = n // 3
        remainder = n % 3

        stack.append(remainder)
        n = quotient

    return stack