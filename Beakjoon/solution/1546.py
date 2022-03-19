# 평균
# https://www.acmicpc.net/problem/1546

"""
    N <= 1000
    score : 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.

    상대오차가 10-2 이하이면 정답이다.
"""
import sys

def solution():
    if N <= 0:
        return
    scores = list(map(int, sys.stdin.readline().split()))
    scores.sort()

    maxScore = scores[-1]

    for idx, score in enumerate(scores):
        scores[idx] = scores[idx] / maxScore * 100

    return sum(scores)/N

# main
N = int(sys.stdin.readline())
print(solution())
