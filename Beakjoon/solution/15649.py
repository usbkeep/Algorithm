# N과 M (1)
# https://www.acmicpc.net/problem/15649

"""
    1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
    (1 ≤ M ≤ N ≤ 8)
"""
import sys

S = []

def dfs():
    if len(S) == M:
        print(' '.join(map(str, S)))
        return
    for i in range(1, N+1):
        if i not in S:
            S.append(i)
            dfs()
            S.pop()
    return

# main
N, M = map(int, sys.stdin.readline().split())
dfs()