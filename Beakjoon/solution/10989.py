# 수 정렬하기 3
# https://www.acmicpc.net/problem/10989

"""
     N(1 ≤ N ≤ 10,000,000)
"""

import sys

N = int(sys.stdin.readline())

numbers = [0 for _ in range(10001)]
for _ in range(N):
    numbers[int(sys.stdin.readline())] += 1

for i, num in enumerate(numbers):
    if num != 0:
        for _ in range(num):
            print(f"{i}")
