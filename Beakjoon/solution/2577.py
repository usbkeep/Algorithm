# 숫자의 개수
# https://www.acmicpc.net/problem/2577

"""
    입력:
        100보다 크거나 같고, 1,000보다 작은 자연수
"""
import sys


# main
counts = [0]*10
number = 1

for _ in range(3):
    number *= int(sys.stdin.readline())
while number:
    counts[number % 10] += 1
    number //= 10

[print(count) for count in counts]
