# N 찍기
# https://www.acmicpc.net/problem/2741

"""
    100,000보다 작거나 같은 자연수 N
"""
import sys

# main
N = int(sys.stdin.readline())

[print(n) for n in range(1, N+1)]
