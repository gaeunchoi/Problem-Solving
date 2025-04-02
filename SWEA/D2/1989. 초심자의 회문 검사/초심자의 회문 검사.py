T = int(input())

for test_case in range(1, T+1):
    message = input()
    reversed_message = message[::-1]
    if message == reversed_message:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')