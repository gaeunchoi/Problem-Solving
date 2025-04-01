def solution(friends, gifts):
    send_gifts_cnt = [[0] * len(friends) for _ in range(len(friends))]
    receive_gifts_cnt = [[0] * len(friends)  for _ in range(len(friends))]
    gift_grade = [0] * len(friends)
    total_gift_cnt = [0] * len(friends)

    for gift in gifts:
        sender, receiver = gift.split()
        send_gifts_cnt[friends.index(sender)][friends.index(receiver)] += 1
        receive_gifts_cnt[friends.index(receiver)][friends.index(sender)] += 1

    print(send_gifts_cnt)
    print(receive_gifts_cnt)

    for i in range(len(gift_grade)):
        gift_grade[i] = sum(send_gifts_cnt[i]) -  sum(receive_gifts_cnt[i])

    for i in range(len(send_gifts_cnt)):
        for j in range(len(send_gifts_cnt[i])):
            if send_gifts_cnt[i][j] > send_gifts_cnt[j][i]:
                total_gift_cnt[i] += 1
            elif send_gifts_cnt[i][j] == send_gifts_cnt[j][i]:
                if gift_grade[i] > gift_grade[j]:
                    total_gift_cnt[i] += 1

    answer = max(total_gift_cnt)
    return answer