# 나이순 정렬
# https://www.acmicpc.net/problem/10814

"""
    1 ≤ N ≤ 100,000
    각 회원의 나이와 이름이 공백으로 구분되어 주어진다.
    1 <= age <= 200
    len(name) <= 100
"""
import sys

# class member:
#
#     def __init__(self, id, age, name):
#         self.id = id
#         self.age = age
#         self.name = name

N = int(sys.stdin.readline().strip())

memberArr = [[] for _ in range(201)]

for id in range(N):
    age, name = sys.stdin.readline().split()
    memberArr[int(age)].append(f"{age} {name}")

for members in memberArr:
    if members:
        if len(members) > 1:
            for m in members:
                print(m)
        else:
            print(members.pop())


"""
# Test Case 1:
3
21 Junkyu
21 Dohyun
20 Sunyoung
result =
20 Sunyoung
21 Junkyu
21 Dohyun
"""