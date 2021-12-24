# 윤년
# https://www.acmicpc.net/problem/2753

"""
    1 <= year <= 4000
"""

import sys

def is_leapYear(year):
    if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
        return 1
    return 0

year = int(sys.stdin.readline().strip())

print(is_leapYear(year))