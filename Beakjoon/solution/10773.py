# 제로
# https://www.acmicpc.net/problem/10773

"""
    1 ≤ K ≤ 100,000
    0 <= n <= 1,000,000, 정수가 0 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
    정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
"""
import sys


# main
K = int(sys.stdin.readline())

stack = []

for _ in range(K):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

print(sum(stack))