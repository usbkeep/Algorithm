# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057

"""
    입출력 예)
        S = "aabbaccc"
        result = 7

        print(solution(S))
"""


def solution(s):

    if (s_len := len(s)) < 3:
        return s_len

    min_len = s_len
    for step in range(1, s_len//2+1):  # step is "1 ~ len(s)//2"
        test = ''
        count = 1
        current = s[:step]

        for i in range(step, s_len, step):
            if current == (next_s := s[i:i + step]):
                count += 1
            else:
                if count > 1:
                    test += str(count) + current
                    count = 1
                else:
                    test += current
            current = next_s
        if count > 1:
            test += str(count) + current
        else:
            test += current

        if min_len > (test_len := len(test)):
            min_len = test_len

    return min_len


print(solution("aabbaccc"))