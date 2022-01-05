# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316

"""
    N <= 100
    단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
"""
import sys
import collections

def is_group(word):
    wordSet = set(word)
    deque = collections.deque(word)

    current = deque.popleft()
    while deque:
        temp = deque.popleft()
        if current == temp:
            pass
        else:
            if current not in wordSet:
                return False
            wordSet.remove(current)
            current = temp

    if current not in wordSet:
        return False

    return True

# main
N = int(sys.stdin.readline().strip())

group_count = 0

for _ in range(N):
    word = sys.stdin.readline().strip()
    if is_group(word):
        group_count += 1

print(group_count)
