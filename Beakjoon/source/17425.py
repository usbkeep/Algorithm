# 약수의 합
# https://www.acmicpc.net/problem/17425
# !특이사항: 백준 사이트에서 제출 시 python3로 제출하면 시간초과만 반복된다. => PyPy3 언어로는 제출 가능.

"""
    테스트 케이스의 개수 T(1 ≤ T ≤ 100,000)
    자연수 N(1 ≤ N ≤ 1,000,000)
"""
import sys
MAX_N = 1000000  # 최댓값

fx = [1] * (MAX_N+1)  # 해당 자연수의 모든 약수를 더한 변수, 1은 모든 수의 약수이다.
dp = [False] * (MAX_N+1)  # 해당 자연수 이하의 모든 fx 값을 더한 변수.


"""
    (i*1, i*2, i*3....)에서 2부터 n까지 i를 약수를 갖는 수를 알 수 있다.

    범위: 2~MAX_N, N = i*j, j= N/i 로 j는 MAX_N/i 까지만 반복한다. 예를 들어 i가 2라면 j는 500,000까지만 계산하면 된다.
    i*j 는 i를 약수로 가지는 수 이다.
    """
for i in range(2, MAX_N + 1):
    j = 1
    while i*j <= MAX_N:
        fx[i * j] += i
        j += 1

# g(x), x보다 작거나 같은 모든 자연수 y의 f(y) 값을 더한 변수
for i in range(1, MAX_N + 1):
    dp[i] += dp[i - 1] + fx[i]

# main
T = int(sys.stdin.readline())

answer = []
for _ in range(T):
    N = int(sys.stdin.readline())
    answer.append(dp[N])
print('\n'.join(map(str, answer)))
