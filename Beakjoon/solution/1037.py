# 약수
# https://www.acmicpc.net/problem/1037

"""
    N의 진짜 약수가 주어진다.
    1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.
    N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
"""
import sys


# main
count = int(sys.stdin.readline())
if count == 1:
    print(int(sys.stdin.readline())**2)
else:
    measures = map(int, sys.stdin.readline().split())
    measures = sorted(measures)
    print(measures[0]*measures[-1])
