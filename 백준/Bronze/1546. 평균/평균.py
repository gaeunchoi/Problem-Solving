n = int(input())
score = list(map(int, input().split()))
max = max(score)

avgscore = [i*100/max for i in score]
print(sum(avgscore) / n)