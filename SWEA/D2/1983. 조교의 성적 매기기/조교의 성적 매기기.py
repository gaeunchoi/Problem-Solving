grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    scores = []
    for i in range(N):
        mid, final, assign = map(int, input().split())
        result = mid * 0.35 + final * 0.45 + assign * 0.2
        scores.append(result)

    target = scores[K-1]
    scores.sort(reverse=True)
    rate = N // 10
    ratio_score = scores.index(target) // rate

    print(f'#{test_case} {grades[ratio_score]}')