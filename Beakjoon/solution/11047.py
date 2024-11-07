# 동전 0
# https://www.acmicpc.net/problem/11047

"""
    N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
    N개의 줄에 동전의 가치 Ai가 "오름차순"으로 주어진다.
    (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)


    K원을 만드는데 필요한 동전 개수의 최솟값
"""
import sys

coinList = []
coinCount = 0

N, K = map(int, sys.stdin.readline().split())

for _ in range(N):
    coinList.append(int(sys.stdin.readline().strip()))

coinList.reverse()

for coin in coinList:
    if K:

        useCoinCount = K//coin
        if useCoinCount > 0:
            coinCount += useCoinCount
            K -= coin * useCoinCount
    else:
        break
print(coinCount)

