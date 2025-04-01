n = int(input())
card = list(map(int, input().split()))

cardcnt = dict()
for i in card:
    if i in cardcnt:
        cardcnt[i] += 1
    else:
        cardcnt[i] = 1

m = int(input())
num = list(map(int, input().split()))

for i in num:
    if i in cardcnt:
        print(cardcnt[i], end = ' ')
    else:
        print(0, end = ' ')