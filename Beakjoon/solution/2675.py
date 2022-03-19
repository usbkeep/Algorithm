# 문자열 반복
# https://www.acmicpc.net/problem/2675

"""
    테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)
    반복 횟수 R(1 ≤ R ≤ 8)
    1 <= len(S) <= 20
"""
import sys


# main
T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    temp = ''

    for c in S:
        temp += c * R
    print(temp)
