for tc in range(1, 11):
    N, messages = input().split()
    messages = list(messages)
    result = []

    for ele in messages:
        if len(result) == 0:
            result.append(ele)
        else:
            if result[-1] == ele:
                result.pop()
            else:
                result.append(ele)

    print(f'#{tc}', end = ' ')
    print(*result, sep = '')