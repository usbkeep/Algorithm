# 최댓값
# https://www.acmicpc.net/problem/2562

"""
    주어지는 자연수는 100 보다 작다.
"""
import sys


# main
max = 0
numbers = [0]

for i in range(1,9+1):
    numbers.append(int(sys.stdin.readline()))
    if numbers[i] > numbers[max]:
        max = i

print(f"{numbers[max]}\n{max}")
