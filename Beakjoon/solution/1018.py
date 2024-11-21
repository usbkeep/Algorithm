# 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018

"""
    자연수, 8 <= N,M <= 50
    Black, White
"""
import sys

def countRepaints(chessBoard, paint):  # count the number of reapints
    count = 0

    for i in range(8):
        for j in range(8):
            if ((i+j)%2 == 0) and (chessBoard[i][j] != paint):  # even numbers, e.g., [0][2], 0+2 = 2
                count += 1
            elif ((i+j)%2 != 0) and (chessBoard[i][j] == paint):  # odd numbers, e.g., [0][1], 0+1 = 1
                count += 1
    return count

def cutChessBoard(x, y):  # cut the board to size 8*8
    for i in range(8):
        for j in range(8):
            chessBoard[i][j] = Board[x + i][y + j]


# main
N, M = map(int, sys.stdin.readline().split())

Board = [None for _ in range(N)]
chessBoard = [[None for _ in range(8)] for _ in range(8)]

for i in range(N):
    line = sys.stdin.readline().strip()
    Board[i] = line

colorArr = ['W', 'B']

if N == M==8:
    result = min(countRepaints(Board, colorArr[0]), countRepaints(Board, colorArr[1]))
else:
    result = N * M
    for i in range(N-7):
        for j in range(M-7):
            cutChessBoard(i, j)
            if result > (r:=min(countRepaints(chessBoard, colorArr[0]), countRepaints(chessBoard, colorArr[1]))):
                result = r
print(result)



"""
--Test Case--
# case 1:
8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
result = 1

# case 2:
18 48
BBBBBWBBBWWWWWBBWWBBBWBBWBWBBBWBWWBWBBBWBWWBBBWB
BBWBBBWBBBWWWWWBBWBWBBBBBBBBBBBBBWWWWWBWWBWWBBWW
WBWWBWBWBBBWBWBBBWWWWBWBBWWWBWWWWWWWWWWBWWWBWBBW
BBWBWBBBBWWWBWWWWBBWBWWBBWWBBBBBWWBWBBBBBBWWBBBW
BBBWBWWBWBBWBBWBWBWBWWBWWBBWWWBWWBBWBBBBWWBBBWBB
WBWBBBWWWWBWWBBWWBWBBWBBBWBWWBBBBWBBBWBWBBWBWWBW
BWWWWBBWBBBBWWWWWBBBBBBBBBBWBBWBWWWWBBBBBWBWWWWW
WBWWBWBBWBBWBBWWBWWWWBWWWWWBBWWWBBWBBWWBWBBWBWWW
BWBWBBWBWBBWWBBBWBWWWWBWBWWBWWBWBWWWBWBBBWBBBBBW
WBWBWBWBWBWWWWWBWWBBWBBWWBBBBBBBBBBBBBWBBWWWWBBW
BBBWBBWBWWBBBWWWWWBBBWBBWBWWWWWBWBWBWBBBBBBBBBWB
WBWBWWWWBBBBBBWWWBBBWWBWWBWWWWWWBBWBBWWBWBBWBWBB
BBWWWWWBBWBBBBWWBBBWBBWWWBBBWWWBWWWWBBWBWWWWWWBB
BBWBBWBWWWBWBWBBWBBBBBWBBWWWWBWBBBWBWBBWBWBWBBWB
BWBWBBWBBWBBWWWBBWBBWBBWBBBWWWBWBBBWWBBWWWWBWBBB
WWWBWBWBWWWBWWBWWBBWWBBBBBBWBWWBWWWBBBBWWBWBBWWW
BBBWBBWBWWBBBBBBWBBBBBWWWBWBBBBWBWWBWWWWWWBWBBBW
BWBWWWWWWWWWWWBBBWWBBBWBBBWBWBBWBBBWBWBWBBWWBBWB
result = 20
"""