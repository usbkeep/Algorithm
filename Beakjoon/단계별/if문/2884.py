# 알람 시계
# https://www.acmicpc.net/problem/2884

"""
    0 ≤ H ≤ 23
    0 ≤ M ≤ 59
"""
import sys

H, M = map(int, sys.stdin.readline().split())

time = (H*60) + M - 45

H = time // 60
M = time % 60

if H < 0:
    H += 24

print(f"{H} {M}")

