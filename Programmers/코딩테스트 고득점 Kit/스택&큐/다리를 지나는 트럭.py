# 다리를 지나는 트럭
# https://programmers.co.kr/learn/courses/30/lessons/42583


"""
    입출력 예)
        bridge_length = 2
        weight = 10
        truck_weights = [7, 4, 5, 6]
        result = 8

        print(solution(bridge_length, weight, truck_weights))
"""


from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = weight
    time = 0

    # truck_weights.reverse()
    truck_weights = truck_weights[len(truck_weights)::-1]

    while truck_weights:
        total_weight += bridge.popleft()

        if total_weight >= truck_weights[-1]:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight -= truck
        else:
            bridge.append(0)

        time += 1

    return time + bridge_length

