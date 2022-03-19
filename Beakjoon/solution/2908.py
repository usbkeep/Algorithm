# 상수
# https://www.acmicpc.net/problem/2908

"""
    두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
"""
import sys
input = sys.stdin.readline

# main
A, B = input().split()

A, B = map(int, [A[::-1],B[::-1]])

print(max(A, B))
