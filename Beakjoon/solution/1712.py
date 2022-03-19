# 손익분기점
# https://www.acmicpc.net/problem/1712

"""
    노트북 판매 대수에 상관없이 매년 임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용
    한 대의 노트북을 생산하는 데에는 재료비와 인건비 등 총 B만원의 가변 비용

    A, B, C는 21억 이하의 자연수이다.
"""
import sys


"""
수입(판매비용)이 총 비용(A + B*count)보다 큰 경우

# A + B * count < C * count
# A < count(C-B) 
# A/(C-B) > count
"""
def solution():

    if C <= B:
        return -1
    else:
        return int(A/(C-B))+1


# main
A, B, C = map(int, sys.stdin.readline().split())

print(solution())
