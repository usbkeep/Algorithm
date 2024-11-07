# https://www.acmicpc.net/problem/10810

"""
    N (1 ≤ N ≤ 100)
    M (1 ≤ M ≤ 100)

    (1 ≤ i ≤ j ≤ N, 1 ≤ k ≤ N)
"""


import sys

def inputBall(basketList, i, j, k):
    i -= 1
    j -= 1
    if i == j:
        basketList[i] = k
    else:
        for index in range(i, j+1, 1):
            basketList[index] = k
    # print(i, j, k, basketList)
    return



N, M = map(int, (sys.stdin.readline().split()))

basketList = [0 for _ in range(N)]

for _ in range(M):
    i, j ,k = map(int, (sys.stdin.readline().split()))
    inputBall(basketList, i, j, k)

print(' '.join(map(str, basketList)))

