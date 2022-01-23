# A+B - 5
# https://www.acmicpc.net/problem/10952

"""
    0 < A, B < 10
"""
import sys

# main
while True:
    A, B = map(int, sys.stdin.readline().split())
    if A == B == 0:
        break
    print(A+B)
