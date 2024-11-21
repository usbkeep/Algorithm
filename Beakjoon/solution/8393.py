# 합
# https://www.acmicpc.net/problem/8393

"""
    (1 ≤ n ≤ 10,000)
"""
import sys

n = int(sys.stdin.readline().strip())

for num in range(1,n):
    n += num

print(n)