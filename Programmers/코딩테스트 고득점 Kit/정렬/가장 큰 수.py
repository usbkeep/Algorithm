# 가장 큰 수
# https://programmers.co.kr/learn/courses/30/lessons/42746

"""
    제한 사항
        1 <= len(numbers) <= 100,000
        0 <= numbers[n] <= 1,000
        return type is str
"""

def solution(numbers):
    if sum(numbers) == 0:  # if numbers == [0,0,0] then return 0
        return '0'

    numbers = list(map(str, numbers))
    """
        ex) 
            numbers = ['1','100'] // result = '1100'
            if len(num) == 1 then len(num) *= 3
            -> ['111','100'].sort()
    """
    numbers.sort(key=lambda x: x*3, reverse=True)

    result = ''.join(numbers)

    return result

def solutionTest():
    # Test case
    numbers = [6, 10, 2],[3, 30, 34, 5, 9],[0,0,0],[3,33,333,330,1000]
    result = "6210", "9534330", "0", "3333333301000"

    for index in range(len(result)):
        actual = solution(numbers[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")

solutionTest()