# 하노이 탑 이동 순서
# https://www.acmicpc.net/problem/11729

"""
    1 ≤ N ≤ 20
"""
import sys

moveHistory = []
K = 0

def move(from_, to_):
    moveHistory.append(f"{from_} {to_}")

def hanoi(number_of_disks_to_move, from_, to_, via_):
    global K
    K += 1
    if number_of_disks_to_move == 1:
        move(from_,to_)
        #print(from_, "->", to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_)
        move(from_, to_)
        #print(from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_)
    return K

N = int(sys.stdin.readline().strip())

print(hanoi(N,1,3,2))

for m in moveHistory:
    print(m)
