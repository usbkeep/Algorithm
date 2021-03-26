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

    return list(participant_dict.keys()).pop(-1)
