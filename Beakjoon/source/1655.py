# 가운데를 말해요
# https://www.acmicpc.net/problem/1655

"""
     1 <= N <= 100,000
     -10,000 <= number <= 10,000
"""

import sys
import heapq


N = int(sys.stdin.readline().strip())
maxHq, minHq = [], []

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if len(maxHq) == len(minHq):
        heapq.heappush(maxHq, -num)
    else:
        heapq.heappush(minHq, num)

    if len(maxHq) >= 1 and len(minHq) >= 1 and maxHq[0] * -1 > minHq[0]:
        maxValue = heapq.heappop(maxHq) * -1
        minValue = heapq.heappop(minHq)

        heapq.heappush(maxHq, minValue * -1)
        heapq.heappush(minHq, maxValue)

    print(maxHq[0] * -1)
    # print(f"max : {maxHq}")
    # print(f"min : {minHq}")
    # print('----')


"""
최소 힙(Min Heap)의 구조
모든 k에 대해 heap[k] <= heap[2*k+1] 또는 heap[k] <= heap[2*k+2] 만족
가장 작은 요소가 heap[0]에 위치
힙을 만들기 위해서는, 초기화된 리스트 []를 사용하거나, heapify를 통해 값이 들어있는 리스트를 힙으로 변환 가능
"""
