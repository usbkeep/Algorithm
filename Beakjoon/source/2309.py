# 일곱 난쟁이
# https://www.acmicpc.net/problem/2309

"""
    아홉 난쟁이의 키가 주어졌을 때
    일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
    정답이 여러 가지인 경우에는 아무거나 출력한다.

    - 입력 -
    일곱 난쟁이의 키를 오름차순으로 출력한다. 일곱 난쟁이를 찾을 수 없는 경우는 없다.
    주어지는 키는 100을 넘지 않는 자연수
"""
import sys

def solution(arr):
    total = sum(arr)  #
    size = len(arr)
    for i in range(size-1):
        for j in range(1,size):
            if (total - (arr[i] + arr[j])) == 100:
                arr[i] = arr[j] = 0
                arr.sort()
                return arr[2:]
    return -1


# - main -
dwarfs = []
for _ in range(9):
    N = int(sys.stdin.readline())
    dwarfs.append(N)

result = solution(dwarfs)

# print result
[print(dwarf) for dwarf in result]