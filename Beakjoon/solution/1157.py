# 단어 공부
# https://www.acmicpc.net/problem/1157

"""
    단어의 길이는 1,000,000을 넘지 않는다.
"""
import sys


# main
S = sys.stdin.readline().strip().upper()
S = sorted(S)

answer = current = ''
maxCount = currentCount = 0

for c in S:
    if not current:
        current = c

    if current == c:
        currentCount += 1
    else:
        current = c
        currentCount = 1

    if maxCount < currentCount:
        answer = current
        maxCount = currentCount
    elif maxCount == currentCount and answer:
        answer = '?'

print(answer)
