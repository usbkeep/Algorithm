# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541

"""
    첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있다
    가장 처음과 마지막 문자는 숫자이다.
    연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
    수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.
"""


# 문제푸는애
import sys
from collections import deque

input = sys.stdin.readline


def stringToNumberic(S : str):
    deq = deque()
    temp=  0
    flag = 0
    for i in S:
        if i not in ('-', '+'):  # 숫자인 경우
            i = int(i)
            if temp == 0:  # 빈 경우
                temp = i
            else:
                temp = temp * 10 + i
        else:
            if flag == 1:
                temp *= -1
            deq.append(temp)
            if i == '-':
                flag = 1
            elif i == '+':
                flag = 0
            temp = 0
    if temp:
        if flag == 1:
            temp *= -1
        deq.append(int(temp))
    return deq
# solution
def solution(S : str):  ### 문제 풀 친구
    deq = stringToNumberic(S)
    result = 0
    temp = 0
    flag = 0  # 음수 연속
    for n in deq:
        if n < 0 or flag == 1:  # 음수로 만들 수 있는 최댓값 계산
            if n > 0:
                n = -n
            temp += n
            flag = 1
        else:  # 양수 출현
            if temp or flag == 1:
                temp -= n
            else:
                temp += n
            result += temp
            temp =  0
    return result + temp


# main
S = input().strip()
print(solution(S))


# # test
# def test():
#     inputS = '55-50+40', '10+20+30+40', '00009-00009', '3-3+3+3'
#     answers = '-35', '100', '0', '-6'
#     for S, answer in zip(inputS, answers):
#         actual = solution(S)
#         answer = int(answer)
#         print(f"expect: {answer} actual:{actual} result={answer == actual}")
# test()

