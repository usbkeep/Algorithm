# 특정한 최단 경로
# https://www.acmicpc.net/problem/1504

"""
    1번 정점에서 N번 정점으로 최단 거리로 이동하려고 한다.

    N과 간선의 개수 E가 주어진다.
    (2 ≤ N ≤ 800, 0 ≤ E ≤ 200,000)
    둘째 줄부터 E개의 줄에 걸쳐서 세 개의 정수 a, b, c가 주어지는데,
    a번 정점에서 b번 정점까지 양방향 길이 존재하며, 그 거리가 c라는 뜻이다.
    (1 ≤ c ≤ 1,000)
    다음 줄에는 반드시 거쳐야 하는 두 개의 서로 다른 정점 번호 v1과 v2가 주어진다.
    (v1 ≠ v2, v1 ≠ N, v2 ≠ 1) 임의의 두 정점 u, v 사이에는 간선이 최대 1개 존재한다.
"""
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

# 무방향 그래프 (양쪽 추가)
graph = [[]for _ in range(N + 1)]
for _ in range(E):
    u, v, distance = map(int, input().split())
    graph[u].append((v, distance))
    graph[v].append((u, distance))
# # check graph
# print(graph)
v1, v2 = map(int, input().split())  # 타켓 두 지점 v1, v2


"""
    v1과 v2를 반드시 거쳐야 한다.
    1 -> v1 -> v2 -> N
    1 -> v2 -> v1 -> N
"""
origin_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = origin_distance[v1] + v1_distance[v2] + v2_distance[N] # 1 -> v1 -> v2 -> N
v2_path = origin_distance[v2] + v2_distance[v1] + v1_distance[N] # 1 -> v2 -> v1 -> N

result = min(v1_path, v2_path)
if result < INF: # 경로 존재
    print(result)
else: # 경로 X
    print(-1)

# test
"""
### case 1, ###
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3
#answer 1, #
7
"""

