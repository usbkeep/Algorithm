# 숫자 카드 2
# https://www.acmicpc.net/problem/10816

"""
    N(1 ≤ N ≤ 500,000)
    M(1 ≤ M ≤ 500,000)
    carNum(-10,000,000 <= carNum <= 10,000,000)
"""

import sys
maxNum = 10000001
def abs(n):
    return n*-1

N = int(sys.stdin.readline())

negativeNum = [0] * maxNum
positiveNum = [0] * maxNum
N_cards = map(int, sys.stdin.readline().split())

for card in N_cards:
    if card < 0:
        negativeNum[abs(card)] += 1
    else:
        positiveNum[card] += 1

M = int(sys.stdin.readline())
M_cards = map(int, sys.stdin.readline().split())

result = []
for card in M_cards:
    if card < 0:
        result.append(negativeNum[abs(card)])
    else:
        result.append(positiveNum[card])

print(*result, sep=" ")