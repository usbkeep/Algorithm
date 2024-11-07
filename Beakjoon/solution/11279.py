# 최대힙
# https://www.acmicpc.net/problem/11279

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

    # heapq, default = min_heap
    x = int(input()) * -1  # (value * -1), min_heap => max_heap
    if x == 0:
        if heap:
            print(f"{heapq.heappop(heap) * -1}")  # print original_value
        else:
            print(f"{0}")
    else:
        heapq.heappush(heap, x)


