# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

import sys
from collections import deque

input = sys.stdin.readline

def printArr(arr):
    print('<', end='')
    if len(arr) >1:
        for i in range(len(arr)-1):
            print(arr[i], end=", ")
    print(f"{arr[-1]}>", end='')

if __name__ == "__main__":
    N, K = map(int, input().split()) # 인원 수 N, target count K
    result = []
    que = deque()

    # make deq
    for n in range(1, N+1):
        que.append(n)

    while que:
        for _ in range(K): # target count
            que.append(que.popleft())
        result.append(que.pop()) # target pop()

    printArr(result)


# test
"""
# case 1 #
7 3
# answer 1 #
<3, 6, 2, 7, 5, 1, 4>
"""

