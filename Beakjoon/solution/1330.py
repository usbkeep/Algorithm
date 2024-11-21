# 두 수 비교하기
# https://www.acmicpc.net/problem/1330

"""
    A와 B는 공백 한 칸으로 구분되어져 있다.
"""

import sys

A, B = map(int, sys.stdin.readline().split())

if A>B:
    result = '>'
elif A<B:
    result = '<'
else:
    result = '=='

print(result)