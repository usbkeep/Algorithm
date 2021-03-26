programmers/ python
 https://programmers.co.kr/learn/courses/30/lessons/42583

# 문제 설명
트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 
트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 
무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다


<img src="https://user-images.githubusercontent.com/78432057/109421139-745daf80-7a19-11eb-8edd-6e84ae41c5fb.PNG">


따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 
이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

# 제한 조건
bridge_length는 1 이상 10,000 이하입니다.
weight는 1 이상 10,000 이하입니다.
truck_weights의 길이는 1 이상 10,000 이하입니다.
모든 트럭의 무게는 1 이상 weight 이하입니다.

# 풀이
<pre><code>
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
</code></pre>

<img src="https://user-images.githubusercontent.com/78432057/109421137-732c8280-7a19-11eb-823c-f23048b97afc.png">
정리: https://blog.naver.com/usbeen/222251723714
