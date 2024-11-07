# 직각삼각형
# https://www.acmicpc.net/problem/4153

"""
    ---
"""

import sys
def NumbersSquared(list : list):  # elements type is int
    for i in range(len(list)):
        list[i] **= 2
    return list

def isRightAngle(triangle: list):

    triangle = NumbersSquared(triangle)  # a**2 + b**2 = c**2

    if triangle[0] + triangle[1] == triangle[2]:
        return "right"
    return "wrong"

while True:
    triangle = sorted(list(map(int, sys.stdin.readline().split())))
    if triangle == [0,0,0]:
        break
    print(isRightAngle(triangle))