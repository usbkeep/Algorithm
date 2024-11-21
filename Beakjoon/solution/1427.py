# 소트인사이드
# https://www.acmicpc.net/problem/1427

"""
     N은 1,000,000,000보다 작거나 같은 자연수이다.
"""
import sys

# main
N = sys.stdin.readline().strip()
sortN = sorted(N, reverse=True)
print(''.join(sortN))