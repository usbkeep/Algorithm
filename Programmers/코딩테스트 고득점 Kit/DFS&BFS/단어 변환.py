# 단어 변환
# https://programmers.co.kr/learn/courses/30/lessons/43163

"""
    제한사항
        각 단어는 알파벳 소문자로만 이루어져 있습니다.
        각 단어의 길이는 3 이상 10 이하이며 모든 단어의 길이는 같습니다.
        words에는 3개 이상 50개 이하의 단어가 있으며 중복되는 단어는 없습니다.
        begin과 target은 같지 않습니다.
        변환할 수 없는 경우에는 0를 return 합니다.
"""
import collections


def is_change(A, target):  # 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
    count = 0
    for a, t in zip(A,target):
        if a != t:
            count +=1
        if count >= 2:
            return False
    return True


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = []
    que = collections.deque([(begin,0)])

    while que:
        word, depth = que.popleft()

        if word not in visited:
            visited.append(word)

            if word == target:
                return depth
            for w in words:
                if (w not in visited) and is_change(word,w):
                    que.append((w,depth+1))
    return 0

def solutionTest():
    # Test Case
    begin = "hit", "hit",
    target = "cog", "cog",
    words = ["hot", "dot", "dog", "lot", "log", "cog"], ["hot", "dot", "dog", "lot", "log"]

    result = 4, 0

    for index in range(len(result)):
        actual = solution(begin[index], target[index], words[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")

solutionTest()