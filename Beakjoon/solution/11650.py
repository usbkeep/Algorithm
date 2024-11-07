# 좌표 정렬하기
# https://www.acmicpc.net/problem/11650

"""
    2차원 평면 위의 점 N개가 주어진다.
    좌표를 x좌표가 증가하는 순으로,
    x좌표가 같으면 y좌표가 증가하는 순서로 정렬

    N (1 ≤ N ≤ 100,000)
    N개의 줄에는 i번점의 위치 xi와 yi
    (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.
"""

import sys

N = int(sys.stdin.readline())

coordinate = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append([x,y])

coordinate.sort(key= lambda x: (x[0], x[1]))

for x, y in coordinate:
    print(x,y)