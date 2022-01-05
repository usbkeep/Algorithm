# 여행 경로
# https://programmers.co.kr/learn/courses/30/lessons/43164
"""
    항상 "ICN" 공항에서 출발합니다.
    제한사항
        모든 공항은 알파벳 대문자 3글자로 이루어집니다.
        주어진 공항 수는 3개 이상 10,000개 이하입니다.
        tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
        주어진 항공권은 모두 사용해야 합니다.
        만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
        모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
"""

from collections import defaultdict

def dfs_travel(routes, start):
    visited = []
    stack = [start]

    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            visited.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())

    return visited


def solution(tickets):

    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    answer = dfs_travel(routes, 'ICN')
    answer.reverse()

    return answer


def solutionTest():
    # Test Case
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]], \
              [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]], \
              [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]], \
              [["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]]

    result = ["ICN", "JFK", "HND", "IAD"], \
             ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"], \
             ["ICN", "B", "ICN", "A", "D", "A"], \
             ["ICN", "AAA", "ICN", "AAA", "ICN", "AAA"]
    solution(tickets[2])
    for index in range(len(result)):
        actual = solution(tickets[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")


solutionTest()