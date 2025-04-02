T = int(input())

for tc in range(1, T+1):
    case = int(input())
    scores = list(map(int, input().split()))
    set_scores = set(scores)

    result = [0, 0]
    for score in set_scores:
        cnt = scores.count(score)

        if result[1] < cnt or result[0] < score and result[1] == cnt:
            result = [score, cnt]
    print(f'#{case} {result[0]}')
