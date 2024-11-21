# 한수
# https://www.acmicpc.net/problem/1065

"""
    N < 1000
"""

import sys

N = int(sys.stdin.readline().strip())

count = 0
for num in range(1,N+1):
    if num <= 99:
        count += 1
    else:
        arr = []
        while num >= 1:
            arr.append(num % 10)
            num = num//10

        # 등차수열인지 비교.
        flag = 0
        for idx in range(len(arr)-2):
            temp = arr[idx] - arr[idx+1]
            if arr[idx+1] - arr[idx+2] != temp:
                flag = 1
                break
        if flag == 0:
            count += 1

print(count)