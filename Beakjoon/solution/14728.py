# 벼락치기
# https://www.acmicpc.net/problem/14728

import sys

input = sys.stdin.readline

def printArr(arr):
    for r in arr:
        print(r)
    return

def knapsack(N, T, itemsT, itemsV): # 아이템 개수 N, 주어진 최대시간 T
    dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]

    for i in range(N+1):
        for t in range(T+1):
            # (가방의 크기 0) or (item is None)
            if i==0 or t == 0:
                pass
            # A = 현재 아이템을 넣을 수 있게 가방을 최적화 했을 경우
            # B = 현재 아이템을 제외한 나머지로 최적화된 값
            # max(A, B)
            elif itemsT[i-1] <= t:
                dp[i][t] = max(itemsV[i-1] + dp[i-1][t-itemsT[i-1]],
                               dp[i-1][t])
            # 현재 뽑은 아이템의 크기가 가방에 들어갈 수 없는 경우, 전 단계 값
            else:
                dp[i][t] = dp[i-1][t]
    # printArr(dp)  # check DP
    return dp[N][T]

if __name__ == "__main__":
    N, T = map(int, input().split()) # 단원 개수 N, 총 시간 T
    itemsT = []
    itemsV = []
    total = 0
    for _ in range(N):
        t, value = map(int, input().split())
        itemsT.append(t) # weight (해당 문제에선 소요시간)
        itemsV.append(value) # value
        total += value
    # print(items) # check items
    result = knapsack(N, T, itemsT, itemsV)
    print(result)

# test
"""
# case 1 #
3 310
50 40
100 70
200 150
# answer 1 #
220
"""

