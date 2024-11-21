# 빠른 A+B
# https://www.acmicpc.net/problem/15552

"""
     T <= 1,000,000
     1 <= A,B <= 1000
"""
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rsplit())
    print(A+B)