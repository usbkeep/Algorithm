# NM과 K (1)
# https://www.acmicpc.net/problem/18290

"""
    선택한 두 칸이 인접하면 안된다. r행 c열에 있는 칸을 (r, c)라고 했을 때,
    (r-1, c), (r+1, c), (r, c-1), (r, c+1)에 있는 칸이 인접한 칸이다.

    1 ≤ N, M ≤ 10
    1 ≤ K ≤ min(4, N×M)
    격자판에 들어있는 수는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
    항상 K개의 칸을 선택할 수 있는 경우만 입력으로 주어진다.
"""
import sys

MIN_NUM = -10000
MAX_NUM = 10000
adjacency = ((0,1)
             ,(0,-1)
             ,(1,0)
             ,(-1,0))

def dfs(x, y, depth, S):

    if depth == K:
        global answer
        answer = max(S, answer)
        return

    for i in range(x, N):
        for j in range(y if i == x else 0, M):
            if visited[i][j]:
                continue

            flag = True
            for aX,aY in adjacency:
                # 인접 확인.
                mX, mY = i+aX, j+aY

                if (0 <= mX < N) and (0 <= mY < M):
                        if visited[mX][mY]:
                            flag = False
                            break
            if flag:
                visited[i][j] = True
                dfs(i, j, depth+1, S+gridPlate[i][j])
                visited[i][j] = False
    return


# main
N, M, K = map(int, sys.stdin.readline().split())
gridPlate = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


answer = MIN_NUM * K
dfs(0,0,0,0)
print(answer)
