# 최소비용 구하기 2
# https://www.acmicpc.net/problem/11779

import heapq
import sys

input = sys.stdin.readline
INF = float("INF")
# dijkstra
def dijkstra(start):
    global graph
    costList = [INF] * (N + 1) # 정점의 개수 N
    prev_node = [0] * (N + 1) # 정점의 개수 N
    q = []
    heapq.heappush(q, (0, start)) # 자신
    costList[start] = 0

    while q:
        weight, node = heapq.heappop(q)  # current node
        if costList[node] < weight:
            continue
        for adj_node, adj_weight in graph[node]:
            cost = weight + adj_weight  # node -> adj_node
            if costList[adj_node] > cost:  # 현재 경로가 더 최적인지 판단
                costList[adj_node] = cost
                heapq.heappush(q, (cost, adj_node))
                prev_node[adj_node] = node

            # # 출력 조건에 경로가 여러개인 경우, 정점의 이름이 더 작은 것으로 출력해야 한다면
            # if costList[adj_node] == cost:
            #     if prev_node[adj_node] > node: # 더 작은 경우, 갱신
            #         prev_node[adj_node] = node
    return costList, prev_node

def findPath(target):
    path = [target]
    now = path[0]
    while now != start:
        now = prev_node[now]
        path.append(now)
    return path
# main
N = int(input())  # 도시의 개수 N
M = int(input())  # 버스의 개수

# 방향 그래프
graph = [[]for _ in range(N + 1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int, input().split())  # root(start) -> target(end)

costList, prev_node = dijkstra(start)
# print(costList, prev_node)

print(costList[end]) # A -> B 최소 비용

path = findPath(end)
print(len(path))

for i in range(len(path)): # 역순으로 출력
    print(f"{path.pop()}", end=' ')

# test
"""
### case 1, ###
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
#answer 1, #
4
3
1 3 5
"""

