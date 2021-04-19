"""
absolutes       signs       result
[4,7,12]  [true,false,true]	  9
[1,2,3]   [false,false,true]	0
"""


def solution(absolutes, signs):
    answer = 0

    for a, s in zip(absolutes, signs):
        if s:
            answer += a
        else:
            answer -= a

    return answer
