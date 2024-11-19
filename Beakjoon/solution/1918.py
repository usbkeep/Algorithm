# 후위 표기식
# https://www.acmicpc.net/problem/1918

import sys

input = sys.stdin.readline

def infixToPostfix(infixNotation):
    # print(f"origin = {infixNotation}")
    operators = {'+':1,
                 '-':1,
                 '*':2,
                 '/':2,
                 '(':3, ')':3}
    opStack = []
    result = []

    for x in infixNotation:
        if x in operators: # 연산자인 경우
            if x == '(':
                opStack.append(x)
            elif x == ')':
                while opStack and opStack[-1] != '(':  # 괄호가 시작된 부분까지 pop
                    result.append(opStack.pop())
                opStack.pop() # remove '('
            else:
                if x in {'*', '/'}:
                    while opStack and operators[opStack[-1]] == operators[x]: # 우선순위가 같다면 pop
                        result.append(opStack.pop())
                    opStack.append(x)
                elif x in {'+', '-'}:
                    while opStack and opStack[-1] != '(':
                        result.append(opStack.pop())
                    opStack.append(x)
        else:
            result.append(x)
    while opStack:
        result.append(opStack.pop())
    return result

# main
if __name__ == "__main__":
    infix_notation = input().strip()
    result = ''.join(infixToPostfix(infix_notation))
    print(result)

"""
    test
"""
def infixToPostfixTests():
    # case 1
    origin = "A*(B+C*D)+E"
    answer = "ABCD*+*E+"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 2
    origin = "A*(B+C)"
    answer = "ABC+*"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 3
    origin = "A+B*C-D/E"
    answer = "ABC*+DE/-"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 4
    origin = "A+B+C"
    answer = "AB+C+"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 5
    origin = "A*B-C*D/E"
    answer = "AB*CD*E/-"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 6
    origin = "(A+B)*(C+D)-E"
    answer = "AB+CD+*E-"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 7
    origin = "A*B*C"
    answer = "AB*C*"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 7
    origin = "A*(B+C)/D"
    answer = "ABC+*D/"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 8
    origin = "A+(B-C)/D"
    answer = "ABC-D/+"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 9
    origin = "A+B*C+D"
    answer = "ABC*+D+"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
    # case 10
    origin = "G*(A-B*(C/D+E)/F)"
    answer = "GABCD/E+*F/-*"
    result = ''.join(infixToPostfix(origin))
    print(f"{result} == {answer} : {answer == result}")
# infixToPostfixTests()

