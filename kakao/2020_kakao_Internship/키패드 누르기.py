# https://programmers.co.kr/learn/courses/30/lessons/67256?language=python3

right_set = {3, 6, 9}
left_set = {1, 4, 7}
decision_set = {2, 5, 8, 11}


def solution(numbers, hand):
    answer = ''
    hand = hand[0].upper()

    # 현재 위치
    r = 12
    l = 10

    for n in numbers:
        if n in right_set:
            r = n
            answer += 'R'
        elif n in left_set:
            l = n
            answer += 'L'
        else:
            if n == 0:
                n = 11
            n_l = current_to_target(l, n)
            n_r = current_to_target(r, n)

            if n_l == n_r:
                if hand == 'R':
                    r = n
                else:
                    l = n
                answer += hand
            elif n_l > n_r:
                r = n
                answer += 'R'
            else:
                l = n
                answer += 'L'

    return answer


def current_to_target(current, target):

    if current not in decision_set:
        if current in right_set:
            current -= 1
        else:
            current += 1
        return (abs(current - target) // 3)+1
    else:
        return abs(current - target) // 3
