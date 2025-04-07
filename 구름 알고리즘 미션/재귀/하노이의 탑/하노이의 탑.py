import sys
input = sys.stdin.readline

def hanoi(n, start, end, via):
    if n == 1:
        return [(start, end)]
    return (hanoi(n - 1, start, via, end) + [(start, end)] + hanoi(n - 1, via, end, start))

# 하노이의 탑 이동 기록
moves = hanoi(20, 1, 3, 2)
K = int(input())

# 막대 상태 초기화
sticks = {1: list(range(20, 0, -1)), 2: [], 3: []}

# K번 이동 시뮬레이션
for start, end in moves[:K]:
    sticks[end].append(sticks[start].pop())

# 각 막대의 원반 크기 합 출력
print(*(sum(sticks[i]) for i in range(1, 4)))