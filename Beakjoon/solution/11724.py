# 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

"""
    정점의 개수 N과 간선의 개수 M이 주어진다.
    (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)

    둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
    (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
"""


#
import sys

input = sys.stdin.readline

# DFS
def DFS(graph : dict, visited : set, root):
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            if graph.get(node):
                stack.extend(graph[node])
                graph.pop(node)
    return visited


# main
# 정점 N, 간선 M
N, M = map(int, input().split())
graph = {}
visited = set()
count = 0  # count network

if M == 0:  # 간선 없는 경우
    print(N)
else:
    # makeGraph
    for i in range(M):
        u, v = map(int, input().split())
        if graph.get(u):
            graph[u].append(v)
        else:
            graph[u] = [v]
        if graph.get(v):
            graph[v].append(u)
        else:
            graph[v] = [u]
    # copy keys
    keys = graph.copy().keys()
    for key in keys:
        if key not in visited:  # 방문하지 않는 노드만 시도
            DFS(graph, visited, key)
            count += 1

    print(count + N - len(visited))  # 연결 되지 않은(간선이 없는) 나머지 요소

# # test
"""
#case 1
6 5
1 2
2 5
5 1
3 4
4 6

# case 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3

# case 3
6 2
3 4
4 2
"""

