# solved.ac
# https://www.acmicpc.net/problem/18110

"""
    절사평균이란 극단적인 값들이 평균을 왜곡하는 것을 막기 위해
    가장 큰 값들과 가장 작은 값들을 제외하고 평균을 내는 것을 말한다.
    30% 절사평균의 경우 위에서 15%, 아래에서 15%를 각각 제외하고 평균을 계산한다.

    제외되는 사람의 수는 위, 아래에서 각각 반올림한다.
    따라서 20명이 투표했다면, 가장 높은 난이도에 투표한 3명과 가장 낮은 난이도에 투표한 3명의 투표는
    평균 계산에 반영하지 않는다는 것이다.
"""

import sys

"""
오사오입(round-to-nearest-even)
반올림에서 5 미만의 숫자는 내림, 5 초과의 숫자는 올림합니다.
5의 앞자리가 홀수인 경우에는 올림을, 짝수인 경우에는 내림을 합니다.

우리가 자주 사용하는 사사오입의 반올림은
4 이하의 숫자는 내림, 5 이상의 숫자는 올림을 하는 반올림
"""

# 오사오입 이슈
def round(n):
    n += 0.5
    return int(n)

def trimmedAverage(list : list):
    length = len(list)
    if length == 0:
        return 0
    elif length == 1:
        return list.pop()

    list.sort()
    cut = round(length * 0.15)
    sum = 0
    for i in range(cut, length-cut):
        sum += list[i]
    length -= cut * 2
    if sum == 0:
        return 0
    return round(sum/length)

levels = []

N = int(sys.stdin.readline())

for i in range(N):
    level = int(sys.stdin.readline())
    levels.append(level)
if N == 0:
    print(0)
else:
    print(trimmedAverage(levels))

