# A+B - 3
# https://www.acmicpc.net/problem/10950

"""
    0 < A, B < 10
"""
import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)