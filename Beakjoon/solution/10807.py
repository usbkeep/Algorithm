# 개수 세기
# https://www.acmicpc.net/problem/10807

import sys

def count_num(numList, target):
    count = 0
    for n in numList:
        if target == n:
            count += 1
    return count

N = int(sys.stdin.readline())
numList = list(map(int, sys.stdin.readline().split()))

v = int(sys.stdin.readline())

print(count_num(numList, v))
