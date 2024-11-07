# 다이얼
# https://www.acmicpc.net/problem/5622

"""
    (문제관련 부가 설명 이미지(다이얼)는 링크주소를 통해 확인)
    전화 번호를 각 숫자에 해당하는 문자로 외운다.
    어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.

    단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.
"""
import sys


input = sys.stdin.readline

buttonList = ['1', 'ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ', '0']
DialDict = dict()


def makeAlphabetDict():
    if DialDict:
        return

    num = 1
    for alphabets in buttonList:
        for alpha in alphabets:
            DialDict[alpha] = num
        num += 1

# main
makeAlphabetDict()
answer = 0

word = list(input().strip())
for c in word:
    if c in DialDict:
        answer += DialDict[c] + 1

print(answer)
