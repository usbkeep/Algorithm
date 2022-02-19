# N과 M (2)
# https://www.acmicpc.net/problem/15650

"""
    1 ≤ M ≤ N ≤ 8
"""
import sys


def recursion(at):

    if len(numList) == M:
        print(' '.join(map(str, numList)))
        return

    for i in range(at, N+1):
        if i not in numList:
            numList.append(i)
            recursion(i+1)
            numList.pop()

    return


# main
N, M = map(int, sys.stdin.readline().split())
numList = []
recursion(1)
