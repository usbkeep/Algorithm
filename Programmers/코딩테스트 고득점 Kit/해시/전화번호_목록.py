# 전화번호 목록
# https://programmers.co.kr/learn/courses/30/lessons/42577

"""
    입출력 예)
        phone_book	                        return
        ["119", "97674223", "1195524421"]	false
        ["123","456","789"]	                true

    print(solution(phone_book))
"""


def solution(phone_book):

    book = {phone for phone in phone_book}

    for phone in book:
        temp = ""
        for n in phone:
            temp += n
            if temp in book and temp != phone:
                return False
    return True
