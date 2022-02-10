# 소수 구하기
# https://www.acmicpc.net/problem/1929

"""
    (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력
"""
import sys

# 에라토스테네스의 체, prime_list
def SieveOfEratosthenes(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


# main
M, N = map(int, sys.stdin.readline().split())

primeList = SieveOfEratosthenes(N+1)

for primeNum in primeList:
    if M <= primeNum <= N:
        print(primeNum)
    elif primeNum > N:
        break
