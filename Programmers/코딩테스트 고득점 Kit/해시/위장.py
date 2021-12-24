# 위장
# https://programmers.co.kr/learn/courses/30/lessons/42578

"""
    스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
    같은 이름을 가진 의상은 존재하지 않습니다.
    clothes의 모든 원소는 문자열로 이루어져 있습니다.
    모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
    스파이는 하루에 최소 한 개의 의상은 입습니다.

    # 풀이
    옷_dict 초기화.
    경우의 수 구하기,
        각각의 옷 수 + 1(안입는경우) 곱해주기.
        ex) 상의 2, 하의2

            상의를 입는경우, 2가지
            상의를 안입는경우.
            = 경우의 수는 2+1인 3가지가 된다.

            결국, (2+1) * (2+1) = 9가 되고 최소 하나는 입기때문에 -1 필요.

    입출력 예)
        clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
        return = 5
    print(solution(clothes))
"""


def solution(clothes):
    answer = 1

    cloth_dict = dict()

    # dict init, input
    for name, type in clothes:
        if cloth_dict.get(type):
            cloth_dict[type] += 1
        else:
            cloth_dict[type] = 1

    # if type == 1, return
    if len(cloth_dict) == 1:
        return len(clothes)

    else:
        for type in cloth_dict:
            answer *= (cloth_dict[type]+1)

    answer -= 1  # nothing X, 최소 한 개의 의상은 입습니다.

    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))