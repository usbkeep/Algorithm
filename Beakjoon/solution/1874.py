# 스택 수열
# https://www.acmicpc.net/problem/1874

import sys

input = sys.stdin.readline


if __name__ == "__main__":
    maxN = 100000
    stack = []
    result = []
    N = int(input())
    now = 1
    flag = True
    for _ in range(N):
        target = int(input())
        while now <= target: # target 까지 오름차순으로 push
            stack.append(now)
            result.append('+')
            now += 1

        if stack[-1] == target: # stack.top() == target
            stack.pop()
            result.append('-')
        else:
            flag = False
            break

    # print result
    if flag:
        for r in result:
            print(r)
    else:
        print("NO")

# test
"""
# case 1 #
8
4
3
6
8
7
5
2
1

# answer 1 #
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
"""

