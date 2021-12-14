# 두 개 뽑아서 더하기
# https://programmers.co.kr/learn/courses/30/lessons/68644

"""
    입출력 예)
        numbers = [2,1,3,4,1]
        result = [2,3,4,5,6,7]

        print(solution(numbers))
"""
# itertools.combinations << check!

def solution(numbers):
    answer = set()

    for n in range(0, len(numbers)-1):
        for n2 in range(n+1, len(numbers)):
            answer.add(numbers[n]+numbers[n2])
    answer = list(answer)
    
    return sorted(answer)
