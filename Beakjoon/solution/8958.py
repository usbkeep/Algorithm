# OX퀴즈
# https://www.acmicpc.net/problem/8958

"""

"""
import sys

def calcScore(result):
    score = 0
    c = 0

    for r in result:
        if r == 'O':
            score += 1 + c
            c += 1
        else:
            c = 0

    return score

# main
N = int(sys.stdin.readline())

for _ in range(N):
    result = sys.stdin.readline().strip()
    print(calcScore(result))
