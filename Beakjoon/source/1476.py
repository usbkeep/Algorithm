# 날짜 계산
# https://www.acmicpc.net/problem/1476

"""
    1 ≤ E ≤ 15,
    1 ≤ S ≤ 28,
    1 ≤ M ≤ 19

"""
import sys
"""
 x mod 15 = E
 x mod 28 = S
 x mod 19 = M

x % 15 = E
x % 28 = S
x % 19 = M
"""

def solution(E, S, M):
    number = 1

    if E==15: E = 0
    if S==28: S = 0
    if M == 19: M = 0

    while True:
        if number%15 == E and number%28==S and number%19==M:
            return number
        number += 1

def solution2(E, S, M):
    Y = S

    while True:
        if Y % 19 == M % 19 and Y % 15 == E % 15:
            break
        Y += 28
    return Y

# main
E, S, M = map(int, sys.stdin.readline().split())

result = solution2(E,S,M)
print(result)


