# 기찍 N
# https://www.acmicpc.net/problem/2742

"""
    100,000보다 작거나 같은 자연수 N
"""
import sys

# main
N = int(sys.stdin.readline())
[print(N-i) for i in range(N)]
