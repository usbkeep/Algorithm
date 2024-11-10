# 문자열 폭발
# https://www.acmicpc.net/problem/9935

"""
    첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다.
    둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
"""
import sys


def solution(S : str, boom):
    stack = []
    i = 0 # index
    while i < len(S):
        stack.append(S[i])  # 원본 문자열 하나씩
        # 스택의 크기가 폭발크기와 같거나 크다면
        if len(stack) >= len(boom):
            # 폭발 여부 판단 및 폭발
            if ''.join(stack[-len(boom):]) == boom:
                for _ in range(len(boom)):
                    stack.pop()
        i += 1 # index += 1

    return stack # 이후 남은 문자열

S = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()

answer = ''.join(solution(S, boom))
if answer:  # 남은 문자열이 존재하는 경우
    print(answer)
else:  # 빈 경우
    print("FRULA")

"""
# case 1, answer = mirkovniz
mirkovC4nizCC44
C4

# case 2, answer = FRULA
12ab112ab2ab
12ab
"""