# IOIOI
# https://www.acmicpc.net/problem/5525

"""
    N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 한다.
    P1 IOI
    P2 IOIOI
    P3 IOIOIOI
    PN IOIOI...OI (O가 N개)
    I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때,
    S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.
"""
import sys

input = sys.stdin.readline

# main
N = int(input())
M = int(input())
S = input().strip()
PN_count = 0  # PN = target = "IOI" + "OI" * (N-1)
i = 0 # index
P1_count = 0  # P1 = IOI

# counting number of PN in S
while i < M - 2:
    if S[i : i+3] == "IOI":
        i += 2
        P1_count += 1
        if P1_count == N:
            PN_count += 1
            P1_count -= 1
    else:
        i += 1
        P1_count = 0
print(PN_count)

# test
"""
# case 1, answer = 4
1
13
OOIOIOIOIIOII

# case 2, answer = 2 
2
13
OOIOIOIOIIOII

# case 3, answer = 2
2
7
IOIOIOI
"""

