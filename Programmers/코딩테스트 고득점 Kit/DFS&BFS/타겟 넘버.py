# 타겟넘버
# https://programmers.co.kr/learn/courses/30/lessons/43165

"""
    제한사항
        주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
        각 숫자는 1 이상 50 이하인 자연수입니다.
        타겟 넘버는 1 이상 1000 이하인 자연수입니다.
"""

def DFS(numbers, target, depth):
    answer = 0

    if depth == len(numbers):
        if sum(numbers) == target:
            return 1
        return 0
    else:
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= -1
        answer += DFS(numbers, target, depth+1)
        return answer


def solution(numbers, target):  # numbers = [1, 1, 1, 1, 1]
    answer = DFS(numbers, target, 0)
    return answer

"""
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
"""
def solutionTest():
    # Test Case
    numbers = [1, 1, 1, 1, 1],
    target = 3,
    result = 5,

    for index in range(len(result)):
        actual = solution(numbers[index], target[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")

solutionTest()