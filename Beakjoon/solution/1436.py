# 영화감독 숌
# https://www.acmicpc.net/problem/1436
"""
    N은 10,000보다 작거나 같은 자연수
"""

import sys

arr_666 = [666,1666,2666,3666,4666,5666]

def find666(arr_666 : list, N):
    num = 5667
    while len(arr_666) < N:
        if N != 0 and len(arr_666) >= N:
            break
        else:
            while len(arr_666) < N:
                num += 1
                if '666' in str(num):
                    arr_666.append(num)
    return arr_666[N-1]

N = int(sys.stdin.readline())

if N == 0:
    print(f"error")
else:
    print(find666(arr_666, N))

