# 약수의 합 2
# https://www.acmicpc.net/problem/17427

"""
    자연수 N(1 ≤ N ≤ 1,000,000)
"""
import sys

def solution(N):
    answer = 0

    for n in range(1, N+1):
        answer += int(N//n) * n
    return answer


def solutionTest():
    numbers = 1, 2, 10, 70, 10000,
    results = 1, 4, 87, 4065, 82256014,

    for number, result in zip(numbers, results):
        actual = solution(number)
        expected = result
        print(f"Expected = {expected} Actual = {actual}, {expected == actual}")


# main
N = int(sys.stdin.readline())
print(solution(N))

#solutionTest()
