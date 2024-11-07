# A + B - C
# https://www.acmicpc.net/problem/31403

"""
    첫 줄에는
    $A, B, C$를 수로 생각했을 때,
    $A+B-C$를 출력하세요.

    둘째 줄에는
    $A, B, C$를 문자열로 생각했을 때,
    $A+B-C$를 출력하세요.
"""

import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
print(A+B-C)

A, B= map(str, [A,B])
print(int(A+B)-C)