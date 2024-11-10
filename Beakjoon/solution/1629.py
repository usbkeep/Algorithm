# 곱셈
# https://www.acmicpc.net/problem/1629

"""
     A, B, C는 모두 2,147,483,647 이하의 자연수
"""

import sys

A, B, C = map(int, sys.stdin.readline().split())

print(pow(A, B, mod=C))

"""
# case 1, answer = 4
10 11 12
"""

