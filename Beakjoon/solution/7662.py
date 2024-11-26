# 이중 우선순위 큐
# https://www.acmicpc.net/problem/7662

import sys
import heapq

input = sys.stdin.readline

# main
T = int(input())  # test case
for t in range(T):
    idSet = set()
    id = 0
    minHeap = []
    maxHeap = []
    K = int(input())  # command count
    for _ in range(K):
        command = input().split()
        command[1] = int(command[1])
        if command[0] == 'I':
            heapq.heappush(minHeap, (command[1], id))
            heapq.heappush(maxHeap, (-command[1], id))
            id += 1

        elif command[0] == 'D':
            if maxHeap and command[1] == 1:
                while maxHeap:
                    max, popId = heapq.heappop(maxHeap)
                    if popId in idSet:
                        continue
                    else:
                        idSet.add(popId)
                        break
            elif minHeap and command[1] == -1:
                while minHeap:
                    min, popId = heapq.heappop(minHeap)
                    if popId in idSet:
                        continue
                    else:
                        idSet.add(popId)
                        break
    minNum = maxNum = 0
    if maxHeap:
        while maxHeap:
            max, popId = heapq.heappop(maxHeap)
            if popId in idSet:
                continue
            else:
                maxNum = -max
                # idSet.add(popId)
                break
    if minHeap:
        while minHeap:
            min, popId = heapq.heappop(minHeap)
            if popId in idSet:
                continue
            else:
                minNum = min
                break

    if maxNum:
        print(maxNum, end=' ')
        print(minNum, end='\n')
    else:
        print("EMPTY")


# test
"""
# case 1 #
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
# answer 1 #
EMPTY
333 -45

# case 2 #
1
5
I 1
D -1
I 1
D 1
I 2
# answer 2 #
2 2

# case 3 #
1
8
D -1
I 1
D 1
I 2
I 3
D 1
I -4
D -1
# answer 3 #
2 2
"""

