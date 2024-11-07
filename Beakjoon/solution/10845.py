# 큐
# https://www.acmicpc.net/problem/10845
"""
    명령은 총 다섯 가지이다.
    push X: 정수 X를 스택에 넣는 연산이다.
    pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 큐에 들어있는 정수의 개수를 출력한다.
    empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
    front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
from collections import deque


def runCommand_que(que : deque, op : str):
    if op == "pop":
        if que:
            return que.popleft()
        return -1
    elif op == "size":
        return len(que)
    elif op == "empty":
        if que:
            return 0
        return 1
    elif op == "front":
        if que:
            return que[0]
        return -1
    elif op == "back":
        if que:
            return que[-1]
        return -1
    else:
        print(f"error")

N = int(sys.stdin.readline())
que = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        que.append(command[1])
    else:
        print(runCommand_que(que, command[0]))
