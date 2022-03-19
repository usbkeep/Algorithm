# 나머지
# https://www.acmicpc.net/problem/3052

"""
    입력:
        0 <= x <=1000
"""
import sys


remainderSet = set()

for _ in range(10):
    remainderSet.add(int(sys.stdin.readline())%42)

print(len(remainderSet))
