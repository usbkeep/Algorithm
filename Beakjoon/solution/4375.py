# 1
# https://www.acmicpc.net/problem/4375

"""
    2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)
    1로만 이루어진 n의 배수
"""
import sys

def solution(n):
    num = 1
    count = 1

    if n==1:
        return count

    while True:
        num = (num *10) + 1
        count += 1
        if num%n == 0:
            return count

#main
while True:
    try:
        n = int(input())
    except EOFError:
        break
    print(solution(n))
