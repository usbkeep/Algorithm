# 리모컨
# https://www.acmicpc.net/problem/1107

"""
    이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)
    고장난 버튼의 개수 M (0 ≤ M ≤ 10)
"""
import sys
MAX_TARGET_CH = 500000


def isPossible(channel, brokenButton):
    channel = str(channel)
    for num in channel:
        if int(num) in brokenButton:
            return False
    return True

def solution(N, brokenButton):
    answer = abs(N-100)

    for channel in range(MAX_TARGET_CH*2):
        if isPossible(channel, brokenButton):
            count = len(str(channel)) + abs(channel - N)
            answer = min(answer, count)

    return answer

# - main -
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
brokenButton = set(map(int,sys.stdin.readline().split()))

print(solution(N, brokenButton))


# - Test -
# def solutionTest():
#     # Test Case
#     targetChannels = 5457, 100, 500000, 100, 14124, 1, 80000,
#     brokenButton = {6,7,8},{0,1,2,3,4}, {0,2,3,4,6,7,8,9}, {1,0,5}, {0}, {1,2,3,4,5,6,7,8,9}, {8,9},
#     results = 6, 0, 11117, 0, 5, 2, 2228,
#
#     for targetChannel, brokenSet, result in zip(targetChannels, brokenButton, results):
#         actual = solution(targetChannel, brokenSet)
#         expected = result
#         print(f"Expected = {expected} Actual = {actual}, {expected == actual}")
# solutionTest()
