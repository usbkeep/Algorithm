# N과 M (4)
# https://www.acmicpc.net/problem/15652

"""
    1 ≤ M ≤ N ≤ 8
"""
import sys

sequence = []

def rec(at):
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(at, N+1):
        sequence.append(i)
        rec(i)
        sequence.pop()

    return


# main
N, M = map(int, sys.stdin.readline().split())
rec(1)
