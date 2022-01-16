# 모의고사
# https://programmers.co.kr/learn/courses/30/lessons/42840

"""
    수포자는 3명이다.

    제한 조건
        시험은 최대 10,000 문제로 구성되어있습니다.
        문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
        가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
"""
from collections import deque

class studentClass:
    def __init__(self, id, answers):
        self.id = id
        self.que = deque(answers)
        self.rightCount = 0

    def use(self):
        answer = self.que.popleft()
        self.que.append(answer)
        return answer

def calcRank(students):
    rank = []

    for student in students:
        if not rank:
            rank.append(student)
        else:
            rankA = rank[-1].rightCount
            B = student
            if rankA < B.rightCount:  # 더 큰경우 최신화.
                rank = [B]
            elif rankA == B.rightCount:  # 동일한 경우
                rank.append(B)

    return [ranker.id for ranker in rank]

def solution(answers):
    studentAnswers = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 수포자 찍는 방법들.
    students = []

    for i in range(3):  # 수포자 3명
        id = i +1
        students.append(studentClass(id, studentAnswers[i]))

    for answer in answers:
        for s in students:
            if answer == s.use():
                s.rightCount += 1
    # # print student, result
    # for student in students:
    #     print(f"student scoreCount : {student.rightCount}, {student.que}")
    # print(f" rank : {calcRank(students)}")

    answer = calcRank(students)
    return answer

def solutionTest():
    # Test Case
    answers = [1,2,3,4,5], [1,3,2,4,2],
    result = [1], [1,2,3]

    for index in range(len(result)):
        actual = solution(answers[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")

solutionTest()