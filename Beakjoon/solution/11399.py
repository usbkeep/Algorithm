# ATM
# https://www.acmicpc.net/problem/11399

"""
    N(1 ≤ N ≤ 1,000)이 주어진다.
    돈을 인출하는데 걸리는 시간 Pi가 주어진다.
    (1 ≤ Pi ≤ 1,000)
"""


# 문제푸는애
import sys


# solution
def solution(pList : list):  ### 문제 풀 친구
    total = []
    # current = 0
    for i, p in enumerate(pList):
        if i == 0:
            total.append(p)
        else:
            total.append(total[i-1] + p)
    return sum(total)


# 메인함수
N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P.sort()

print(solution(P))

