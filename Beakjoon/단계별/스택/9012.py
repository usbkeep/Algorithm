# 괄호
# https://www.acmicpc.net/problem/9012

"""
    괄호 문자열(Parenthesis String, PS) = '(', ')'
    올바른 괄호 문자열(Valid PS, VPS)
    2<= string <= 50
"""
import sys

PS = '(', ')'

def is_VPS(string):
    stack = []

    for c in string:
        if stack and (stack[-1] == PS[0] and c == PS[1]):
            stack.pop()
        else:
            stack.append(c)
    if stack:
        return "NO"
    return "YES"

def main():
    # main
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        string = sys.stdin.readline().strip()
        print(is_VPS(string))


def is_VPSTest():
    string = "(())())", "(((()())()", "(()())((()))", "((()()(()))(((())))()", "()()()()(()()())()", "(()((())()(", \
             "((", "))", "())(()",
    result = "NO", "NO", "YES", "NO", "YES", "NO", "NO", "NO", "NO",

    for index in range(len(result)):
        actual = is_VPS(string[index])
        expected = result[index]
        print(f"correct : {actual} == {expected}, {expected == actual}")

#is_VPSTest()
main()