# 소인수분해
# https://www.acmicpc.net/problem/11653

"""
    1 ≤ N ≤ 10,000,000
"""
import sys

def solution(N):
    r = int(N**0.5)
    i = 2

    while i <= r:
        if N % i == 0:
            print(i)
            N //= i
        else:
            i += 1

    if N > 1:
        print(N)
    return

# main
N = int(sys.stdin.readline())
solution(N)


#Test
def solution2(N):
    i = 2
    while N > 1:
        if N % i == 0:
            print(i)
            N //= i
        else:
            i += 1
    return

def solutionTest():
    from _form.LogAspect import LogExecutionTime
    @LogExecutionTime
    def sol1(N):
        solution(N)
    @LogExecutionTime
    def sol2(N):
        solution2(N)



