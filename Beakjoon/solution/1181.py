# 단어 정렬
# https://www.acmicpc.net/problem/1181

"""
    1 ≤ N ≤ 20,000
    len(string) <= 50
"""
import sys


# main
N = int(sys.stdin.readline().strip())

words = set()

for _ in range(N):
    words.add(sys.stdin.readline().strip())

# 1. 길이가 짧은 것부터\ 2. 길이가 같으면 사전 순으로.
words = sorted(sorted(words),key=lambda x:len(x))

print("\n".join(words))
