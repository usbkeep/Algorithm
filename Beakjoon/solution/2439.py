# 별 찍기 - 2
# https://www.acmicpc.net/problem/2439

"""
    1 ≤ N ≤ 100
"""
import sys

def countingStar(num):
        temp = ' '
        star = '*'
        return (temp*(N-num)) + (star*num)

# main
N = int(sys.stdin.readline().strip())

[print(countingStar(i)) for i in range(1,N+1)]


