import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    mix_count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + second * 2)
        mix_count += 1
    return mix_count