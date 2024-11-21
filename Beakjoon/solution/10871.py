# X보다 작은 수
# https://www.acmicpc.net/problem/10871

"""
    (1 ≤ N, X ≤ 10,000)
"""
import sys

def solution(numbers, X):
    numbers = sorted(numbers, key=lambda x: x < X, reverse=True)
    for n in numbers:
        if n < X:
            print(n, end=' ')
        else:
            return
def solution1(numbers, X):
    for n in numbers:
        if n < X:
            print(n)
    return

# main
N, X = map(int, sys.stdin.readline().split())
numbers = [n for n in sys.stdin.readline().split() if int(n)<X]
print(' '.join(numbers))

#numbers = list(map(int, sys.stdin.readline().split()))
#solution(numbers, X)

