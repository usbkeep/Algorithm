# 좌표 압축
# https://www.acmicpc.net/problem/18870

"""
    1 ≤ N ≤ 1,000,000
    -10^9 ≤ Xi ≤ 10^9
"""
import sys
import collections

N = int(sys.stdin.readline().strip())

numbers = list(map(int, sys.stdin.readline().split()))
sortNumbers = sorted(numbers)

numDict = collections.defaultdict()

count = 0
numDict[sortNumbers[0]] = count

for idx in range(1,len(sortNumbers)):
    num = sortNumbers[idx]
    if numDict.get(num):
        pass
    elif num > sortNumbers[idx-1]:
        count += 1
        numDict[sortNumbers[idx]] = count
    else:
        numDict[sortNumbers[idx]] = count

for num in numbers:
    print(numDict[num], end=' ')