# 베스트앨범
# https://programmers.co.kr/learn/courses/30/lessons/42579

"""
    입출력 예)
        genres = ["classic", "pop", "classic", "classic", "pop"]
        plays = [500, 600, 150, 800, 2500]
        return = [4, 1, 3, 0]

	print(solution(genres, plays))
"""


def solution(genres, plays):
    answer = []

    g_dict = dict()
    p_dict = dict()

    for index, (g, p) in enumerate(zip(genres, plays)):
        if g not in g_dict:
            g_dict[g] = [(index, p)]
        else:
            g_dict[g].append((index, p))

        if g not in p_dict:
            p_dict[g] = p
        else:
            p_dict[g] += p

    for (k, v) in sorted(p_dict.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(g_dict[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer