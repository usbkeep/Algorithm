# 덩치
# https://www.acmicpc.net/problem/7568

"""
    2 ≤ N ≤ 50
    10 ≤ x, y ≤ 200
"""
import sys

class person:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

def size_compare(A, B):
    if A == B:
        pass
    elif (A.weight > B.weight) and (A.height > B.height):
        return True
    return False


# main
N = int(sys.stdin.readline().strip())

people = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())  # weight, height
    people.append(person(x, y))

for p1 in people:
    count = 1
    for p2 in people:
        if size_compare(p2, p1):
            count += 1

    print(count, end=' ')



""" 
# NlogN으로 풀고자 했으나 실패, n^2. 이후에 다시 확인해보자.
# +브루트 포스 << 
Test Case
3
90 180
100 190
110 200
---
correct = 3 2 1
============
3
20 110
16 100
12 90
---
correct = 1 2 3
============
6
8 9
10 8
40 3
4 5
2 54
39 4
---------
correct = 1 1 1 3 1 1, actual = 1 1 1 3 1 1
============
4
10 20
10 20
20 30
20 20
-answer-
correct = 2 2 1 1, actual= 2 2 1 1
"""