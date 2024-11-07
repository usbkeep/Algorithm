# 색종이
# https://www.acmicpc.net/problem/2563
"""
    가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
    이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를
    색종이의 변과 도화지의 변이 평행하도록 붙인다.
    이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후
    색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

    색종이의 수는 100 이하
    색종이가 도화지 밖으로 나가는 경우는 없다
"""


# 문제푸는애
import sys
input = sys.stdin.readline

def isOverlap(arr : list, x, y):  ### 문제 풀 친구
    count = 0
    for i in range(1,11):
        for j in range(1,11):
            arr[x+i][y+j] += 1
            if arr[x+i][y+j] == 1: # 오버랩 부분 카운트
                count +=1
    return count

# 메인함수
arr= [[0 for _ in range(100)] for _ in range(100)]


N = int(input())
overlap_size = 0
for _ in range(N):
    i, j = map(int, input().split())
    i, j = i-1, j-1
    overlap_size += isOverlap(arr, i, j)

print(overlap_size)

