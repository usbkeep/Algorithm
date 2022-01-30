# 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

"""
    (0 ≤ N ≤ 500)
    N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수
"""

import sys

factorial_dict = dict()

def factorial(num):

    if num <= 1:
        return 1
    else:
        if r := factorial_dict.get(num):
            return r
        else:
            factorial_dict[num] = num * factorial(num-1)
            return num * factorial(num-1)

N = int(sys.stdin.readline().strip())
N = factorial(N)

count = 0
while N > 0:
    if N % 10 != 0:
        print(count)
        break
    else:
        N = N//10
        count += 1