# 사분면 고르기
# https://www.acmicpc.net/problem/14681

"""

"""
import sys

x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y>0:
    print(2)
else:
    print(3)