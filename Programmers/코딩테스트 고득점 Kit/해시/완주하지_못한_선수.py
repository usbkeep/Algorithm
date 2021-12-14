# 완주하지 못한 선수
# https://programmers.co.kr/learn/courses/30/lessons/42576

"""
    입출력 예)
        participant = ["leo", "kiki", "eden"]
        completion = ["eden", "kiki"]
        return = "leo"

    print(solution(participant, completion))
"""


def solution(participant, completion):
    participant_dict = dict()

    for p in participant:
        participant_dict[p] = participant_dict.get(p, 0) + 1

    for c in completion:
        value = participant_dict[c] -1

        if value == 0:
            del participant_dict[c]
        else:
            participant_dict[c] = value

    answer = list(participant_dict.keys())

    return answer.pop()
