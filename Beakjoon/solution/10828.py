# 스택
# https://www.acmicpc.net/problem/10828
"""
    명령은 총 다섯 가지이다.
    push X: 정수 X를 스택에 넣는 연산이다.
    pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    size: 스택에 들어있는 정수의 개수를 출력한다.
    empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

import sys
class stack():
    def __init__(self):
        self.value = []
    def push(self, n):
        self.value.append(n)
    def pop(self):
        if not self.empty():
            return self.value.pop()
        else:
            return -1
    def size(self):
        return len(self.value)
    def empty(self):
        if self.value:
            return 0
        return 1
    def top(self):
        if self.empty():
            return -1
        return self.value[-1]

def runCommand_stack(stack : stack, op : str):
    if op == "pop":
        return stack.pop()
    elif op == "size":
        return stack.size()
    elif op == "empty":
        return stack.empty()
    elif op == "top":
        return stack.top()
    else:
        print(f"error")

N = int(sys.stdin.readline())
stack = stack()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.push(command[1])
    else:
        print(runCommand_stack(stack, command[0]))
