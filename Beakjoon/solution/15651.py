# N과 M (3)
# https://www.acmicpc.net/problem/15651

"""
    1부터 N까지 자연수 중에서 M개를 고른 수열
    같은 수를 여러 번 골라도 된다.

    1 ≤ M ≤ N ≤ 7
"""
import sys

sequence = []

def rec():
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(1, N + 1):
        sequence.append(i)
        rec()
        sequence.pop()


# main
N, M = map(int, sys.stdin.readline().split())
rec()
