# 큐 2
# https://www.acmicpc.net/problem/18258

"""
     1 ≤ N ≤ 2,000,000
"""
import sys
from collections import deque


def queOp(command):
    op = command[0]
    if op == 'push':
        que.append(command[1])
    elif op == 'pop':
        if not que:
            print('-1')
        else:
            print(que.popleft())
    elif op == 'size':
        print(len(que))
    elif op == 'empty':
        if len(que) == 0:
            print('1')
        else:
            print('0')
    elif op == 'front':
        if que:
            print(que[0])
        else:
            print('-1')
    elif op == 'back':
        if que:
            print(que[-1])
        else:
            print('-1')


# main
N = int(sys.stdin.readline().strip())

que = deque()

for _ in range(N):
    command = sys.stdin.readline().split()
    queOp(command)
