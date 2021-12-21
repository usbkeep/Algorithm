# 신나는 함수 실행
# https://www.acmicpc.net/problem/9184

"""

"""
import sys

max_size = 21
dp = [[[None for _ in range(max_size)]for _ in range(max_size)] for _ in range(max_size)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if dp[a][b][c] is not None:
        pass
    elif a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")