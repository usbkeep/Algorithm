# 최소비용 구하기
# https://www.acmicpc.net/problem/1916
"""
"""
import sys
import heapq

input = sys.stdin.readline

def daijkstra(start):
    global graph
    prevList = [False] * (N + 1)
    costList = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    costList[start] = 0

    while q:
        weight, node = heapq.heappop(q)
        if costList[node] < weight:
            continue
        if graph.get(node):
            for adj_c, adj_n in graph[node]:
                cost = weight + adj_c
                if costList[adj_n] > cost: # 최단 거리일 경우 갱신
                    prevList[adj_n] = node
                    costList[adj_n] = cost
                    heapq.heappush(q, (cost, adj_n))
    # print(costList, prevList)
    return costList, prevList

# main
INF = float("INF")
N = int(input())
M = int(input()) # 버스의 개수

# graph = [0] * (N + 1)
graph = dict()
for _ in range(M):
    u, v, cost = map(int, input().split())
    #if graph[u]:
    if graph.get(u):
        graph[u].append((cost, v))
    else:
        graph[u] = [(cost, v)]

start, end = map(int, input().split())

costList, prevList = daijkstra(start)
print(costList[end])


# test
"""
# case 1 #
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
# answer 1 #
4
"""

