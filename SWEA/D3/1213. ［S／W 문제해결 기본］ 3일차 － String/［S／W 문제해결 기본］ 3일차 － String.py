T = 10

for tc in range(1, T+1):
    case = int(input())
    target = input()
    message = input()

    t_len = len(target)
    m_len = len(message)

    result = 0

    for i in range(m_len - t_len + 1):
        if message[i] == target[0]:
            if message[i : i + t_len] == target:
                result += 1

    print(f'#{case} {result}')