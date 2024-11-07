# 최소힙
# https://www.acmicpc.net/problem/1927

"""

"""


# 문제푸는애
import sys
import heapq
input = sys.stdin.readline


# 메인함수
N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if heap:
            print(f"{heapq.heappop(heap)}")
        else:
            print(f"{0}")
    else:
        heapq.heappush(heap, x)
