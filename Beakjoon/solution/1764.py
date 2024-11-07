# 듣보잡
# https://www.acmicpc.net/problem/1764

"""
    듣도 못한 사람의 수 N
    보도 못한 사람의 수 M

     N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름

     !출력
     듣보잡의 수와 그 명단을 사전순으로 출력한다.
"""
import sys

N, M = map(int, sys.stdin.readline().split())

d = set()
b = set()

for _ in range(N):
    d.add(sys.stdin.readline().strip())
for _ in range(M):
    b.add(sys.stdin.readline().strip())

db = sorted(list(d & b))
print(len(db))
for dbPerson in db:
    print(dbPerson)

