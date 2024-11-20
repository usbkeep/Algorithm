# 별 찍기 - 11
# https://www.acmicpc.net/problem/2448

import sys

input = sys.stdin.readline


def addStar(star):
    length = len(star)
    board = []

    for s in star:
        board.append(' ' * length + s + ' ' * length)
    for s in star:
        board.append(s + ' ' + s)

    return board


if __name__ == "__main__":
    # 3 * 2**k, (0<=k<=10)
    NumSet = set()
    for k in range(11):
        NumSet.add(3*2**k)
    print(NumSet)
    N = int(input())
    stars = ['  *  ',
             ' * * ',
             '*****']

    if N in NumSet:
        while len(stars) != N:
            stars = addStar(stars)
        [print(f"{s}") for s in stars]
