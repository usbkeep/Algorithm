# 집합
# https://www.acmicpc.net/problem/11723

"""

    add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
    remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
    check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
    toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
    all: S를 {1, 2, ..., 20} 으로 바꾼다.
    empty: S를 공집합으로 바꾼다.


    연산의 수 M (1 ≤ M ≤ 3,000,000)
"""

import sys

S = set()

# op = operator
def calculator(S, op, x):
    x = int(x)

    if op == 'add':
        S.add(x)
    elif op == 'remove':
        if x in S:
            S.remove(x)
    elif op == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif op == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    return


M = int(input())
for _ in range(M):
    command = sys.stdin.readline().split()

    if command[0] == "all":
        S = set(range(1, 21))
    elif command[0] == "empty":
        S.clear()
    else:
        op, x = command[0], command[1]
        calculator(S, op, x)
