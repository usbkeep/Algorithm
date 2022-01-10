# 카드2
# https://www.acmicpc.net/problem/2164

"""
    1 ≤ N ≤ 500,000
"""
import sys
from collections import deque

N = int(sys.stdin.readline().strip())

cards = deque([x+1 for x in range(N)])

while len(cards) > 1:
    # 제일 위에 있는 카드를 버린다.
    cards.popleft()

    # 제일 위에 있는 카드를 맨 뒤로.
    cards.append(cards.popleft())

print(cards.pop())