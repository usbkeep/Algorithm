# A → B
# https://www.acmicpc.net/problem/16953

"""
    정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
     - 2를 곱한다.
     - 1을 수의 가장 오른쪽에 추가한다.
    A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

    A, B (1 ≤ A < B ≤ 10**9)가 주어진다.
"""
import sys
from collections import deque

input = sys.stdin.readline

#
def findTarget(root, target):
    depth_dict = {}
    que = deque([root])
    depth_dict[root] = 0

    while que:
        node = que.popleft()
        if node == target:  # if find target
            break
        elif node > target:
            break
        else:  #
            if node*2 <= target:
                que.append(node * 2)
                depth_dict[node * 2] = depth_dict[node] + 1
            if node*10+1 <= target:
                que.append(node * 10 + 1)
                depth_dict[node * 10 + 1] = depth_dict[node] + 1

    if depth_dict.get(target):
        return depth_dict.get(target) + 1
    return -1



# main
#MAXNUM = 10 ** 9
A, B = map(int, input().split())
answer = findTarget(A, B)
print(answer)


# test
"""
# case 1, answer = 5
#2 → 4 → 8 → 81 → 162 
2 162

# case 2, answer = -1
4 42

# case 3, answer = 5
# 100 → 200 → 2001 → 4002 → 40021
100 40021

# case 4, answer = 1
# 11 -> 111
11 111
"""

