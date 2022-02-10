# 골드바흐의 추측
# https://www.acmicpc.net/problem/6588

"""
    짝수인 정수 n (6 ≤ n ≤ 1000000)
    입력의 마지막 줄에는 0이 하나 주어진다.

    n = a + b 형태로 출력한다. 이때, a와 b는 홀수 소수이다.
"""
import sys

MAX_N = 1000000

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


oddPrimeNumbers = [num for num in SieveOfEratosthenes(MAX_N+1) if num%2 != 0]
oddPrimeNumSet = set(oddPrimeNumbers)

# - main -
while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    flag = True
    for i in range(n//2):
        b = n - oddPrimeNumbers[i]
        if b in oddPrimeNumSet:
            print(f"{n} = {oddPrimeNumbers[i]} + {b}")
            flag = False
            break
    if flag:
        print("Goldbach's conjecture is wrong.")
