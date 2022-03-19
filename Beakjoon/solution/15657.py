# N과 M (8)
# https://www.acmicpc.net/problem/15657

"""
    N개의 자연수 중에서 M개를 고른 수열
    같은 수를 여러 번 골라도 된다.
    고른 수열은 비내림차순이어야 한다.
    길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

    첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
    둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.
"""
import sys

sequence = []

def rec():
    if len(sequence) == M:
        print(' '.join(map(str, sequence)))
        return

    for num in numbers:
        if not sequence or num >= sequence[-1]:
            sequence.append(num)
            rec()
            sequence.pop()
    return


# main
N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()
rec()
