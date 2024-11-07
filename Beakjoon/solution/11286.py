# 절댓값 힙
# https://www.acmicpc.net/problem/11286

"""
    배열에 정수 x (x ≠ 0)를 넣는다.
    배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
    절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
    프로그램은 처음에 비어있는 배열에서 시작하게 된다.
"""


# 문제푸는애
import sys
import heapq

input = sys.stdin.readline


# main
heap = []
abs_dict = {}

N = int(input())

for i in range(N):
    x = int(input())

    if not abs_dict.get(x):
        abs_dict[x] = 0
    abs_dict[x] += 1

    if x == 0:
        if heap:
            pop_v = heapq.heappop(heap)
            if abs_dict.get(-pop_v): # 해당 값의 음수 존재 체크
                abs_dict[-pop_v] -= 1
                pop_v *= -1
            else:  # 양수일 경우
                abs_dict[pop_v] -= 1
            print(f"{pop_v}")  # print original_value
        else:
            print(f"{0}")
    else:
        heapq.heappush(heap, abs(x))


