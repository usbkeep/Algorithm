# 너의 평점은
# https://www.acmicpc.net/problem/25206

"""
    전공평점은 전공과목별 (학점 × 과목평점)의 합을 학점의 총합으로 나눈 값이다.
    A+	4.5
    A0	4.0
    B+	3.5
    B0	3.0
    C+	2.5
    C0	2.0
    D+	1.5
    D0	1.0
    F	0.0

    P/F 과목의 경우 등급이 P또는 F로 표시
    등급이 P인 과목은 계산에서 제외해야 한다.
"""


# 문제푸는애
import sys

# solution
def solution():  ### 문제 풀 친구

    return

gradeDict = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
    }

# 메인함수
gradeS = 0
sum = 0

while True:
    try:
        name, n, grade = sys.stdin.readline().split()
        if grade != 'P':
            gradeS += float(n) * gradeDict[grade]
            sum += float(n)
    except Exception as e:
        # print(e)
        break

print(f"{gradeS/sum}")


