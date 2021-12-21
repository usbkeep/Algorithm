# 신나는 함수 실행
# https://www.acmicpc.net/problem/9184

"""

"""
import sys

w_dict = dict()

def w(a,b,c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif not w_dict.get((a,b,c)):
        if a > 20 or b > 20 or c > 20:
            w_dict[(a,b,c)] = w(20, 20, 20)

        elif a < b and b < c:
            w_dict[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

        else:
            w_dict[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return w_dict[(a, b, c)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a,b,c)}")