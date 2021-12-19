# 검문
# https://www.acmicpc.net/problem/2981

"""
    1 <= num <= 1,000,000,000
    2 ≤ N ≤ 100
    1 < M
"""

import sys
import math

#최대공약수, 유클리드 호제법
def get_gcd(a, b):

    if b==0:
        return a
    else:
        return get_gcd(b,a%b)

# divisors of number
def get_divisors(num):
    divisor_list = []
    sqrt_num = int(math.sqrt(num))
    for i in range(1, sqrt_num + 1):  # ex) num=16, sqrt(16) = 4, 4*4 = num
        if num % i == 0:
            divisor_list.append(i)
            if (d := num // i) != i:
                divisor_list.append(d)

    divisor_list.sort()

    return divisor_list


# main, input
numbers = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    numbers.append(num)
numbers.sort(reverse=True)

# 풀이과정
"""
num1 = M * a1 + r
num2 = M * a2 + r
# remainder, r-r = 0

=> (num1 - num2) =  M(a1-a2)

(a1-a2) are divisors of (num1-num2) 
"""

gcd = 0

for i in range(len(numbers)-1):  # num1-num2, num2-num3, ...
    if gcd == 0:
        gcd = numbers[i] - numbers[i+1]
    else:
        gcd = get_gcd(gcd, numbers[i]-numbers[i+1])

gcd_divisors = get_divisors(gcd)[1:]

for divisor in gcd_divisors:
    print(divisor, end=' ')