# 단어 뒤집기
# https://testhttps://www.acmicpc.net/problem/9093
"""
     단어는 영어 알파벳으로만 이루어져 있다.
    단어의 길이는 최대 20, 문장의 길이는 최대 1000이다
"""
import sys

def reverseWordsToString(words):

    for i, word in enumerate(words):
        #words[i] = word[::-1]
        words[i] = ''.join(reversed(word))

    return ' '.join(words)

def reverseWordsTest():
    words = 'I am happy today', 'We want to win the first prize',
    results = 'I ma yppah yadot', 'eW tnaw ot niw eht tsrif ezirp',
    for words, result in zip(words, results):
        actual = reverseWordsToString(words.split())
        expected = result
        print(f"Expected = {expected} Actual = {actual}, {expected == actual}")

def main2():
    N = int(sys.stdin.readline())

    for i in range(N):
        sentence = sys.stdin.readline()[::-1]
        store = sentence.split()
        store.reverse()
        sentence_reverse = ' '.join(store)
        print(sentence_reverse)

def main():
    # main
    T = int(sys.stdin.readline())
    for _ in range(T):
        words = sys.stdin.readline().split()
        reverseWordsToString(words)
        print(' '.join(words))

main2()
#reverseWordsTest()




