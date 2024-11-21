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
# Test Case 1 :
6
8 9
10 8
40 3
4 5
2 54
39 4
correct : actual = "1 1 1 3 1 1", expected = "1 1 1 3 1 1"

# Test Case 2 :
4
10 20
10 20
20 30
20 20
correct : actual = "2 2 1 1", expected = "2 2 1 1"
"""