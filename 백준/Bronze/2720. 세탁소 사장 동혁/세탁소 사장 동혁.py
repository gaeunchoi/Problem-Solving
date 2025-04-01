import sys

T = int(input())

coin = [25, 10, 5, 1]
for i in range(T):
    coin_cnt = [0, 0, 0, 0]

    C = int(sys.stdin.readline())

    for i in range(len(coin)):
        coin_cnt[i] = C // coin[i]
        C -= coin[i] * coin_cnt[i]

    for i in range(len(coin_cnt)):
        print(coin_cnt[i], end = ' ')