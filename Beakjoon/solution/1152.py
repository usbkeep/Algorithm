# 단어의 개수
# https://www.acmicpc.net/problem/1152

"""
    단어는 공백 한 개로 구분되며, 공백이 연속해서 나오는 경우는 없다. 또한 문자열은 공백으로 시작하거나 끝날 수 있다.
"""
import sys


# main
S = sys.stdin.readline().strip().split(' ')
if S[-1] == '':
    S.pop()

print(len(S))
