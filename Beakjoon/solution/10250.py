# ACM 호텔
# https://www.acmicpc.net/problem/10250

"""

"""
import sys
input = sys.stdin.readline

# main
T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:  # h의 배수이면,
        num = N//H
        floor = H
    else:
        num = N // H + 1
        floor = N % H

    print(f'{floor*100+num}')


# # test
# inputList = [[1,1,1],[2,2,4],[2,2,2],[1,10,10],[10,10,100]]
# for H, W, N in inputList:
#     print(f"H = {H} W = {W} N = {N}")

