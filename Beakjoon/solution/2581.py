# 소수
# https://www.acmicpc.net/problem/2581
"""
입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.
    M과 N은 10,000이하의 자연수이며,
    M <= N
"""
import sys

input = sys.stdin.readline

# 에라토스테네스의 체, prime_list
def SieveOfEratosthenes(N):
    N += 1
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * N

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, N, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, N) if sieve[i] == True]


# main
M = int(input())
N = int(input())

primeNum_sum = 0
min_index = 0
primeNums = SieveOfEratosthenes(N)
# print(primeNums)
for i in range(1, len(primeNums) + 1):
    if primeNums[-i] >= M:
        primeNum_sum += primeNums[-i]
    else:
        min_index = -i+1
        break
if primeNum_sum:
    print(primeNum_sum)
    print(primeNums[min_index])
else:
    print(-1)


# test
"""
### case 1, ###
60
100
#answer 1, #
620
61

### case 2, ###
64
65
#answer 2, #
-1
"""

