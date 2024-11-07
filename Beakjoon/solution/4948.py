# 베르트랑 공준
# https://www.acmicpc.net/problem/4948

"""
    1 ≤ n ≤ 123,456
"""
import sys
input = sys.stdin.readline

"""
n보다 크고, 2n보다 작거나 같은 소수의 개수
"""
def SieveOfEratosthenes(n):
    # 에라토스테네스의 체 초기화
    sieve = [True] * n * 2

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n*2 ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, n*2, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return [i for i in range(2, n*2) if sieve[i] == True]

def CountingPrimeNums(minNum, maxNum):
    count = 0
    for primeNum in PrimeNumbers:
        if minNum < primeNum <= maxNum:
            count +=1
        elif primeNum > maxNum:
            break

    return count


# main
Numbers = []

try:
    while True:
        N = int(input())
        if N == 0:
            break
        Numbers.append(N)
except:
    print(-1)

PrimeNumbers = SieveOfEratosthenes(max(Numbers))

for num in Numbers:
    print(CountingPrimeNums(num, num * 2))
