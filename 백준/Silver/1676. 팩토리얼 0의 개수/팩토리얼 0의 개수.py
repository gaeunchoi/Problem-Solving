N = int(input())

# 10! = 1 2 3 4 5 6 7 8 9 10 -> 2(5, 10 = 2 * 5니까)
# 5! = 1 2 3 4 5 -> 1
# 3! = 1 2 3 -> 0
# 5로 나눠지는 몫이 답

cnt = 0

while N >= 5:
    cnt += N // 5

    N //= 5

print(cnt)