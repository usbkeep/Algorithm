# 평균은 넘겠지
# https://www.acmicpc.net/problem/4344

"""
    C : test case
    1 ≤ N ≤ 1000, N은 정수,
    N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

    각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""
import sys

def solution(scoreList):
    length = scoreList[0]
    scoreList = scoreList[1:]
    count = 0

    avg = sum(scoreList)/length

    for score in scoreList:
        if score > avg:
            count += 1

    return format(count/length, "0.3%")

# main
C = int(sys.stdin.readline())


for _ in range(C):
    students = list(map(int, sys.stdin.readline().split()))
    print(f"{solution(students)}")
