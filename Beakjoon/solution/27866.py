# 문자와 문자열
# https://www.acmicpc.net/problem/27866

"""
    S의 i번째 글자를 출력한다
"""

import sys

S = sys.stdin.readline().strip()
i = int(sys.stdin.readline())

print(S[i-1])