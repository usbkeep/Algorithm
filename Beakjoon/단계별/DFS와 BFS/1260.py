# DFS와 BFS
# https://www.acmicpc.net/problem/1260

"""
    첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000),
    간선의 개수 M(1 ≤ M ≤ 10,000),
    탐색을 시작할 정점의 번호 V가 주어진다.
    다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
    어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
    입력으로 주어지는 간선은 양방향이다.

"""

import sys
import collections


Group = dict()

# DFS
def DFS(root):
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if Group.get(node):
                stack.extend(sorted(list(Group[node]), reverse=True))

    return visited

# BFS
def BFS(root):
    visited = []

    que = collections.deque([root])

    while que:
        node = que.popleft()
        if node not in visited:
            visited.append(node)
            if Group.get(node):
                que.extend(sorted(list(Group[node])))

    return visited

def print_visited(visited):

    for v in visited:
        print(f"{v}",end=' ')
    print()
    return


N, M, V = map(int,sys.stdin.readline().split())

for i in range(M):
    vertex, edge = map(int,sys.stdin.readline().split())
    if Group.get(vertex):
        Group[vertex].add(edge)
    else:
        Group[vertex] = {edge}
    if Group.get(edge):
        Group[edge].add(vertex)
    else:
        Group[edge] = {vertex}


print_visited(DFS(V))
print_visited(BFS(V))