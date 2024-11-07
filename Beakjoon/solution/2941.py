# 크로아티아 알파벳
# https://www.acmicpc.net/problem/2941

"""
    최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
"""
import sys
input = sys.stdin.readline

CroatiaAlphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

def countingCroatianAlphabets(word):

    for croatia in CroatiaAlphabets:
        word = word.replace(croatia, '1')

    return len(word)

def countingCroatianAlphabetsTest():
    inputS = 'ljes=njak', 'ddz=z=', 'nljj', 'c=c=', 'dz=ak',
    answers = 6,3,3,2,3,
    for S, answer in zip(inputS, answers):
        actual = countingCroatianAlphabets(S)
        print(f"expect: {answer} actual:{actual} result={answer == actual}")
# Test
# countingCroatianAlphabetsTest()

# main
S = input().strip()
print(countingCroatianAlphabets(S))
