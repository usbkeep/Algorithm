# 수 찾기
# https://www.acmicpc.net/problem/1920

"""
    N(1 ≤ N ≤ 1,000,000)이 주어진다.
    둘째 줄부터 N개의 줄에는 수가 주어진다.
    이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다.
    수는 중복되지 않는다.
"""

import sys


N = int(sys.stdin.readline())
numberSet = set(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

for num in numbers:
    if num in numberSet:
        print(1)
    else:
        print(0)