# 평범한 배낭
# https://www.acmicpc.net/problem/12865

"""
    (1 ≤ N ≤ 100), (1 ≤ K ≤ 100,000)
    (1 ≤ W ≤ 100,000), (0 ≤ V ≤ 1,000)
"""

import sys

# knapsack problem, algorithm
def knapsack_calc(K, N, items):

    dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

    for i in range(N+1):
        for w in range(K+1):
            if i==0 or w==0:
                dp[i][w] = 0
            elif (items[i-1][0] <= w) and (w-items[i-1][0] >= 0):  #
                dp[i][w] = max(items[i-1][1] + dp[i-1][w-items[i-1][0]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[N][K]


# main
N, K = map(int, sys.stdin.readline().split())  # 물건 갯수 N, 배낭 무게 K

items = []

for _ in range(N):  # 물건 갯수 N
    W, V = map(int, sys.stdin.readline().split())  # weight, value
    items.append((W,V))

print(knapsack_calc(K,N,items))
