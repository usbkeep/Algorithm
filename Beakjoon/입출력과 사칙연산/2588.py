# 곱셈
# https://www.acmicpc.net/problem/2588

"""
    (세 자리 수) * (세 자리 수)
"""

import sys


A = int(sys.stdin.readline().strip())
B = int(sys.stdin.readline().strip())

print(A*(B%10))
print(A*((B//10)%10))
print(A*(B//100))
print(A*B)