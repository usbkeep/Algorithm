# 시험 성적
# https://www.acmicpc.net/problem/9498

"""
    0 <= x <= 100
"""

import sys

score = int(sys.stdin.readline().strip())

if score >= 90:
    result = 'A'
elif score >= 80:
    result = 'B'
elif score >= 70:
    result = 'C'
elif score >= 60:
    result = 'D'
else:
    result = 'F'

print(result)