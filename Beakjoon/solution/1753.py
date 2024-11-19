# 최단경로
# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline

# dijkstra
def dijkstra(start):
    distanceList = [INF] * (N + 1) # 정점의 개수 N
    q = []
    heapq.heappush(q, (0, start)) # 자신
    distanceList[start] = 0

    while q:
        dist, current = heapq.heappop(q)
        if distanceList[current] < dist:
            pass
        for v, d in graph[current]:
            distance = dist + d
            if distanceList[v] > distance:
                distanceList[v] = distance
                heapq.heappush(q, (distance, v))
    return distanceList


# main
#INF = float('inf')
INF = int(1e9)

N, E = map(int, input().split()) # 정점의 개수 N, 간선의 개수 E
root = int(input()) # root

# 방향 그래프
graph = [[]for _ in range(N + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# # check graph
# print(graph)

"""
    모든 정점 방문하기
    못가는  경우 INF
"""
origin_distance = dijkstra(root)
# print(origin_distance)


for i in range(1, N+1):
    if i == root:  # 자신일 때는 0 출력
        print("0")
    else:
        result = origin_distance[i]
        if result < INF: # 경로 존재
            print(result)
        else: # 경로 X
            print("INF")

# test
"""
### case 1, ###
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
#answer 1, #
0
2
3
7
INF
"""

