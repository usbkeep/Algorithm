# 친구 네트워크
# https://www.acmicpc.net/problem/4195

"""
    친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다.
    친구 관계는 두 사용자의 아이디로 이루어져 있으며,
    알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열
"""
import sys

input = sys.stdin.readline

# find parent
def find(p): # p (parent)
    if p == parent[p]:
        return p
    else:
        parent[p] = find(parent[p])
        return parent[p]

# a + b
def union(a, b):
    # find parent
    a = find(a)
    b = find(b)
    # if a_parent == b_parent
    if a == b:
        pass
    else:
        parent[b] = a
        network[a] += network[b]
    return

if __name__ == "__main__":
    network = dict()
    parent = dict()
    T = int(input())

    for t in range(T):
        F = int(input())
        for f in range(F):
            a, b = input().split()
            if a not in parent:
                parent[a] = a
                network[a] = 1
            if b not in parent:
                parent[b] = b
                network[b] = 1
            union(a, b)
            root = find(a)
            result = network[root]
            print(result)
        parent.clear()
        network.clear()

# test
"""
### case 1, ###
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty
#answer 1,#
2
3
4
2
2
4
"""

