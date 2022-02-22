# N과 M (7)
# https://www.acmicpc.net/problem/15656

"""
    1 ≤ M ≤ N ≤ 8
    입력으로 주어지는 수는 10,000보다 작거나 같은 자연수
"""
import sys

sequence = []

def rec():
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for i in range(len(numbers)):
        num = numbers[i]
        sequence.append(num)
        rec()
        sequence.pop()

    return


# main
N, M = map(int, sys.stdin.readline().split())

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

rec()
