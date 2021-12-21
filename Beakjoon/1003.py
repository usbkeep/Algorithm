# 피보나치 함수
# https://www.acmicpc.net/problem/1003

"""
    fibonacci(N)을 호출했을 때
    fibonacci(0), fibonacci(1) count.
"""

import sys

fibo_dict = {0:0, 1:1}

def fibo(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    elif fibo_dict.get(num):
        return fibo_dict[num]
    else:
        fibo_dict[num] = fibo(num-1) + fibo(num-2)
        return fibo_dict[num]


T = int(sys.stdin.readline().strip())
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    if N ==0:
        print(f"1 {fibo(N)}")
    else:
        print(f"{fibo(N-1)} {fibo(N)}")
