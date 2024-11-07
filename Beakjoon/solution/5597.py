# 과제 안 내신 분..?
# https://www.acmicpc.net/problem/5597
"""
    입력은 총 28줄로 각 제출자(학생)의 출석번호 n(1 ≤ n ≤ 30)가 한 줄에 하나씩 주어진다.
    출석번호에 중복은 없다.

    출력은 2줄이다.
    1번째 줄엔 제출하지 않은 학생의 출석번호 중 가장 작은 것을 출력
    2번째 줄에선 그 다음 출석번호를 출력
"""
import sys


studentNumbers = set()

for i in range(28):
    n = int(sys.stdin.readline())
    studentNumbers.add(n)

count = 0
for n in range(1, 31):
    if n not in studentNumbers:
        print(n)
        count += 1
    if count == 2:
        break

