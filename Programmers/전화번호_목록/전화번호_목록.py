def solution(phone_book):

    book = {phone for phone in phone_book}

    for phone in book:
        temp = ""
        for n in phone:
            temp += n
            if temp in book and temp != phone:
                return False
    return True
