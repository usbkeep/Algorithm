# 프린터
# https://programmers.co.kr/learn/courses/30/lessons/42587

"""
제한사항
    1 <= len(priorities) <= 100
    인쇄 작업의 중요도는 숫자가 클수록 중요하다는 뜻입니다.
    location index 관련, 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.
"""

import collections

def solution(priorities, location):
    answer = 0
    queue = collections.deque(enumerate(priorities))

    while queue:

        idx, p = queue.popleft()

        if any(p < max_p for max_idx, max_p in queue):
            queue.append((idx, p))
        else:
            answer += 1
            if idx == location:
                break

    return answer

def solutionTest():
    priorities = [2, 1, 3, 2],[1, 1, 9, 1, 1, 1]
    location = 2,0
    result = 1,5

    index = 1
    print(f"{solution(priorities[index], location[index])} == {result[index]} ?")

solutionTest()