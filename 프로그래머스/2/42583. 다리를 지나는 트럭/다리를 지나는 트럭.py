from collections import deque
def solution(bridge_length, weight, truck_weights):
    t = 0       # 소요시간
    bridge = deque([0] * bridge_length)     # 다리 위

    current_weight = 0
    while truck_weights:
        t += 1

        current_weight -= bridge.popleft()
        if current_weight + truck_weights[0] <= weight:
            current_weight += truck_weights[0]
            bridge.append(truck_weights.pop(0))
        else:
            bridge.append(0)

    t = t + bridge_length
    return t