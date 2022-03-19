# 주사위 세개
# https://www.acmicpc.net/problem/2480

"""
    같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
    같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
    모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
"""
import sys


def calcReward():
    reward = 0
    # 모두 다른 경우 maxNum * 100
    if (l := len(set(numbers))) == 3:
        reward = max(numbers) * 100

    # 같은 눈 3개인 경우, 10000 + num*1000
    elif l == 1:
        reward = 10000 + numbers[0] * 1000

    # 같은 눈이 2개인 경우, 1000 + 같은 눈*100
    elif l == 2:
        if numbers[0] == numbers[1]:
            reward = 1000 + numbers[0] * 100
        else:
            reward = 1000 + numbers[2] * 100
    return reward


# main
numbers = list(map(int, sys.stdin.readline().split()))
counts = [0] * 7

for num in numbers:
    counts[num] += 1

print(calcReward())
