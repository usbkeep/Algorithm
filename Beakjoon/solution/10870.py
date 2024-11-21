# 피보나치 수 5
# https://www.acmicpc.net/problem/10870

"""
    자연수, 0 <= n <= 20
"""
import sys

def fibonacci(num):
    if num <= 1:
        return num
    elif dp[num] is not None:
        return dp[num]
    else:
        dp[num] = fibonacci(num-1) + fibonacci(num-2)
        return dp[num]


n = int(sys.stdin.readline().strip())

dp = [None for _ in range(n+1)]

print(fibonacci(n))

