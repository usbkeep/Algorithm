# 알파벳 찾기
# https://www.acmicpc.net/problem/10809

"""
    S: 단어
    0 <= len(S) < 100
    알파벳 소문자로만 이루어져 있다.

"""
import sys


alphabet = [-1 for _ in range(ord('z') - ord('a') + 1)]

S = sys.stdin.readline().strip()
base = ord('a')

for i, c in enumerate(S):
    if alphabet[ord(c) - base] == -1:
        alphabet[ord(c) - base] = i

print(' '.join(map(str, alphabet)))
