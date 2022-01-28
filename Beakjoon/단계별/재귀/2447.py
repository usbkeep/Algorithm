# 별 찍기 - 10
# https://www.acmicpc.net/problem/2447

"""
    (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다.

    N은 3의 거듭제곱이다.
    즉 어떤 정수 k에 대해 N=3^k이며, 이때 1 ≤ k < 8이다.
"""
import sys
sys.setrecursionlimit((3**7) +5)  # test 결과 +5 필요, 다른 환경에서도 실행해보자.
# print(sys.getrecursionlimit())

def countingStars(N):
    if N == 1:
        return ['*']
    stars = countingStars(N // 3)
    line = []

    for s in stars:
        line.append(s*3)
    for s in stars:
        line.append(s +' ' * (N // 3) + s)
    for s in stars:
        line.append(s*3)

    return line

#main
N = int(sys.stdin.readline())
print('\n'.join(countingStars(N)))







