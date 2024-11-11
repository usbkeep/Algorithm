# 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

"""
    수 N개가 주어졌을 때,
    i번째 수부터 j번째 수까지 합

    1 ≤ N ≤ 100,000
    1 ≤ M ≤ 100,000
    1 ≤ i ≤ j ≤ N
"""
import sys

input = sys.stdin.readline


# main
N, M = map(int, input().split())
nList = [0]
nList.extend(list(map(int, input().split())))
#print(nList)

# make sum arr
sum_arr = []
temp = 0
for n in nList:
    temp += n
    sum_arr.append(temp)
for _ in range(M):
    i, j = map(int, input().split())
    print(f"{sum_arr[j] - sum_arr[i-1]}")

# test
"""
##case 1, 
5 3
5 4 3 2 1
1 3
2 4
5 5
#answer 1,
12
9
1
"""

