# 비밀번호 찾기
# https://www.acmicpc.net/problem/17219

"""
    사이트 주소의 수 N(1 ≤ N ≤ 100,000)
    비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)

"""

import sys

N, M = map(int, sys.stdin.readline().split())

pwDict = dict()

for i in range(N):
    website, pw = sys.stdin.readline().split()
    pwDict[website] = pw

for i in range(M):
    website= sys.stdin.readline().strip()
    print(pwDict[website])
