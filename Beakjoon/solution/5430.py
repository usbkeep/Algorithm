# AC
# https://www.acmicpc.net/problem/5430

import sys
from collections import deque

input = sys.stdin.readline

def calc(arr, operators):
    errorFlag = 0
    reverseFlag = False
    for op in operators:
        if op == 'R':
            reverseFlag = not reverseFlag
        elif op == 'D':
            if arr:
                if not reverseFlag:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                errorFlag = 1
                break
    if errorFlag:
        print("error")
    else:
        if reverseFlag:
            arr.reverse()
        print(f"[{','.join(arr)}]")
    return

# main
T = int(input()) # 테스트 케이스의 개수 T

for t in range(T):
    operators = input().strip() # 수행할 함수 p
    n = int(input()) # 배열의 크기 n
    arr = deque(input().strip()[1:-1].split(sep=',', maxsplit=-1))  # 배열 및 덱으로 변환
    if n == 0:
        arr = deque()
    # print(f"{type(arr)} : {arr}") # check arr
    calc(arr, operators)


# test
"""
### case 1, ###
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]

#answer 1, #
[2,1]
error
[1,2,3,5,8]
error
"""

