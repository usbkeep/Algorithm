# 셀프 넘버
# https://www.acmicpc.net/problem/4673

"""
    n, d(n), d(d(n)), d(d(d(n))), ...과 같은 무한 수열을 만들 수 있다.
    e.g. 33 + 3 + 3 = 39

    10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력
"""

dArr = [False] * 10001
selfNumSet = set()

def d(num):
    if dArr[num] or num > 10000:
        return

    result = sum(list(map(int , list(str(num))))) + num

    dArr[num] = result

    if result <= 10000:
        selfNumSet.add(result)
    return

# main

for x in range(10001):
    d(x)

for x in range(10001):
    if x not in selfNumSet:
        print(x)
