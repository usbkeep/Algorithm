# Fly me to the Alpha Centauri
# https://www.acmicpc.net/problem/1011

"""
    테스트케이스의 개수 T가 주어진다.
    각각의 테스트 케이스에 대해 현재 위치 x 와 목표 위치 y 가 정수로 주어지며,
    (0 ≤ x < y < 231)

    # K[n] = K[n-1]-1 or K[n-1] or K[n-1]+1
    # K[start] = 1
    # K[end] = 1
"""

import sys
import math

T = int(sys.stdin.readline().strip())
count_list = []
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y-x
    max_move = math.sqrt(distance)

    if max_move > (m:= int(max_move)):
        if max_move - m > 0.5:
            count_list.append((m*2)+1)
        else:
            count_list.append(m*2)
    else:
        count_list.append((m*2)-1)

for count in count_list:
    print(count)
