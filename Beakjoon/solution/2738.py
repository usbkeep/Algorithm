# 행렬 덧셈
# https://www.acmicpc.net/problem/2738
"""
    첫째 줄에 행렬의 크기 N 과 M이 주어진다.
    둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 차례대로 주어진다.

    이어서 N개의 줄에 행렬 B의 원소 M개가 차례대로 주어진다.
    N과 M은 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.
"""
import sys


n, m = map(int, sys.stdin.readline().split())
matrix_1 = []
matrix_2 = []

# matrix_1
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    matrix_1.append(row)

# matrix_2
for _ in range(n):
    row = list(map(int, sys.stdin.readline().strip().split()))
    matrix_2.append(row)

# print(f"{matrix_1}\n{matrix_2}") # check (matrix_1 and matrix_2)

result = [] # result = matrix_1 + matrix_2
for i in range(n):
    sum_row = []
    for m_1, m_2 in zip(matrix_1[i], matrix_2[i]):
        sum_row.append(m_1 + m_2)
    result.append(sum_row[i])

for row in result:
    print(' '.join(map(str, row)))
