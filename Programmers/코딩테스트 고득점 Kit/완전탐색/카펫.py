# 카펫
# https://programmers.co.kr/learn/courses/30/lessons/42842

"""
제한사항
    갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
    노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
    카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.
"""

def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2))+1):
        if yellow % i == 0:
            if 2*(i + yellow//i) == brown-4:
                return [yellow//i+2, i+2]

def solutionTest():
    # Test Case
    brown = 10, 8, 24,
    yellow = 2, 1, 24,
    result = [4,3], [3,3], [8,6],

    for index in range(len(result)):
        actual = solution(brown[index], yellow[index])
        expected = result[index]
        print(f"Expected = {expected} Actual = {actual}, {expected == actual}")

solutionTest()