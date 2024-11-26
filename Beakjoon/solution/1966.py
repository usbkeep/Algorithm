# 프린터 큐
# https://www.acmicpc.net/problem/1966

import sys
from collections import deque


input = sys.stdin.readline

def printTarget(documents, targetIndex):
    result = []
    documentsDict = dict()
    q = deque()
    indexQ = deque()
    # input index, documents
    for i, p in enumerate(documents):
        indexQ.append(i)
        q.append(p)
        if documentsDict.get(p):
            documentsDict[p] += 1
        else:
            documentsDict[p] = 1
    priority = sorted(documentsDict.keys())

    while q:
        p = q.popleft()
        i = indexQ.popleft()
        if priority and priority[-1] == p: # 중요도가 가장 큰 경우
            result.append(i)
            # if target document
            if i == targetIndex:
                break
            documentsDict[p] -= 1
            if documentsDict[p] == 0:
                documentsDict.pop(p)
                priority.pop()
        else: # 남아있는 문서 중 중요도가 더 큰 것이 존재하는 경우
            q.append(p)
            indexQ.append(i)
    return result

# main
T = int(input())
for t in range(T):
    N, M = map(int, input().split())  # 문서의 개수 N, 타겟 위치 M
    documents = map(int, input().split())
    result = printTarget(documents, M)
    print(len(result))


# test
"""
# case 1 #
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1

# answer 1 #
1
2
5
"""
