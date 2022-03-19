# 오븐 시계
# https://www.acmicpc.net/problem/2525

"""
    시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)

    요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위
"""
import sys


# main
A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

minutes = A*60 + B + C
h, m = divmod(minutes, 60)
h %= 24
print(f"{h} {m}")
