# 바이러스
# https://www.acmicpc.net/problem/2606

"""
    computer_count <= 100
    1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
"""
import sys

def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if graph.get(node) is not None:
                stack.extend(graph[node])
    return visited


computer_count = int(sys.stdin.readline().strip())
edge_count = int(sys.stdin.readline().strip())

graph = dict()


#init graph
for _ in range(edge_count):
    com_info = sys.stdin.readline().split()

    if len(com_info) == 2:
        com1, com2 = com_info
        if graph.get(com1):
            graph[com1].append(com2)
        else:
            graph[com1] = [com2]

        if graph.get(com2):
            graph[com2].append(com1)
        else:
            graph[com2] = [com1]
    else:
        graph[com_info] = None

result = DFS(graph, '1')
print(len(result)-1)