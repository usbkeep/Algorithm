# 랜선 자르기
# https://www.acmicpc.net/problem/1654

"""
    랜선의 개수 K, 그리고 필요한 랜선의 개수 N이 입력

    K는 1이상 10,000이하의 정수이고, N은 1이상 1,000,000이하의 정수
"""


# 문제푸는애
import sys

def floatToInt(n : float):
    return int(n+0.5)
def isPossibleCut(key, lines : list, goal):
    count = 0
    for line in lines:
        count += line//key
    if goal <= count:
        return True
    return False

# solution
def solution(low, high, lines : list, N):  ### 문제 풀 친구
    maxLength = 0
    while low <= high:
        mid = floatToInt((high + low)/2)
        if isPossibleCut(mid, lines, N):
            low = mid+1
        else:
            high = mid-1
        maxLength = high

    return maxLength


# 메인함수
K, N = map(int, sys.stdin.readline().split())

lines = []
low = 1
high = 0
for i in range(K):
    line = int(sys.stdin.readline())
    if high < line:
        high = line
    lines.append(line)
# print(f"{low}, {high}")
print(solution(low, high, lines, N))


