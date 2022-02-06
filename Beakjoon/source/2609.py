# 최대공약수와 최소공배수
# https://www.acmicpc.net/problem/2609

"""
    10,000이하의 자연수
"""
import sys

# GCD
def GreatestCommonDivisor(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return GreatestCommonDivisor(n, m%n)

# LCM
def LeastCommonMultiple(m, n, gcd):
    return m * n / gcd


# main
M, N = map(int, sys.stdin.readline().split())
gcd = GreatestCommonDivisor(M,N)
print(gcd)

lcm = int(LeastCommonMultiple(M, N, gcd))
print(lcm)
