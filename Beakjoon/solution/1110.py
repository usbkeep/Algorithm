# 더하기 사이클
# https://www.acmicpc.net/problem/1110

"""
    정수, 0 <= N <= 99
"""
import sys

def solution(N):
    answer = N
    count = 0

    while True:
        if N >= 10:  # 26
            N = ((N % 10) * 10) + ((N // 10) + (N % 10)) % 10
        else:
            N = N * 11
        count += 1

        if N == answer:
            break
    return count

def solutionTest():
    # Test Case
    N = 26, 55, 1, 0, 71
    result = 4, 3, 60, 1, 12

    for index in range(len(result)):
        actual = solution(N[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")

# solutionTest()

# main
N = int(sys.stdin.readline().strip())
print(solution(N))

