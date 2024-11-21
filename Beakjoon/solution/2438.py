# 별 찍기 - 1
# https://www.acmicpc.net/problem/2438

"""
    1 ≤ N ≤ 100
"""
import sys

# main
N = int(sys.stdin.readline().strip())

star = '*'

for i in range(1, N+1):
    print(star*i)

