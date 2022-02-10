# 사탕 게임
# https://www.acmicpc.net/problem/3085

"""
    N×N크기
    보드의 크기 3 ≤ N ≤ 50
    빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
"""
import sys


def checkScore(board):
    N = len(board)
    score = 0

    # 가로
    for i in range(N):
        count = 0
        temp = board[i][0]
        for j in range(N):
            if temp == board[i][j]:
                count += 1
            else:
                count = 1
                temp = board[i][j]

            if count > score:
                score = count

    # 세로
    for j in range(N):
        count = 0
        temp = board[0][j]
        for i in range(N):
            if temp == board[i][j]:
                count += 1
            else:
                count = 1
                temp = board[i][j]

            if count > score:
                score = count
    return score

def solution(board):
    answer = 0
    N = len(board)
    for i in range(N):
        for j in range(N-1):

            # <열(col), 세로>
            if (i<N-1) and (board[i][j] != board[i+1][j]):
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # swap
                score = checkScore(board)
                board[i][j], board[i+1][j] = board[i+1][j], board[i][j]  # 복구
                answer = max(answer, score)
            # </열(col), 세로>


            # <행(row), 가로>
            if (board[i][j] != board[i][j+1]):
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # swap
                score = checkScore(board)
                board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 복구
                answer = max(answer, score)
            # </행(row), 가로>
    return answer


# main
N = int(sys.stdin.readline())
board = [[] for _ in range(N)]
for i in range(N):
    board[i] = list(sys.stdin.readline().strip())

print(solution(board))