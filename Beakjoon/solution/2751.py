# 수 정렬하기 2
# https://www.acmicpc.net/problem/2751

"""
    N(1 ≤ N ≤ 1,000,000)이 주어진다.
    둘째 줄부터 N개의 줄에는 수가 주어진다.
    이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다.
    수는 중복되지 않는다.
"""

import sys

numbers = []
N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    numbers.append(num)
numbers.sort()

for num in numbers:
    print(num)