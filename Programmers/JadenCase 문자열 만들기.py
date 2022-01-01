# programmers
# https://programmers.co.kr/test

"""
    제한 조건
        s는 길이 1 이상인 문자열입니다.
        s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
        첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )
"""


def solution(s):
    if len(s) == 1:
        return s.upper()
    answer = ''

    s = s.split(' ')

    for temp in s:
        if temp == '':
            answer += ' '
        else:
            answer += temp[0].upper() + temp[1:].lower() + ' '

    answer = answer[:-1]
    return answer

def solutionTest():
    # Test Case
    s = "3people unFollowed me", "for the last week", "aaaaa aaa", "a   bcd  hello"
    result = "3people Unfollowed Me", "For The Last Week", "Aaaaa Aaa", "A   Bcd  Hello"

    for index in range(len(result)):
        actual = solution(s[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")

solutionTest()