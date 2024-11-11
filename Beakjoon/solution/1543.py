# 문서 검색
# https://www.acmicpc.net/problem/1543

"""
    문서의 길이는 최대 2500
    검색하고 싶은 단어의 길이는 최대 50이다.

    문서와 단어는 알파벳 소문자와 공백으로 이루어져 있다.
"""


# 문제푸는애
import sys
from collections import deque

# solution
def solution(S : deque, target : deque):
    result = 0
    temp = deque()
    while S:
        temp.append(S.popleft())
        if len(temp) == len(target):
            if temp == target:
                result += 1
                temp.clear()
            else:
                temp.popleft()

    return result


# main
S = list(sys.stdin.readline().strip())
S = deque(S)
target = deque(list(sys.stdin.readline().strip()))

print(solution(S, target))

