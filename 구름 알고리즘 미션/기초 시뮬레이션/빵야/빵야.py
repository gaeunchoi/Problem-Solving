N = int(input())
H = list(map(int, input().split(" ")))
result = 0
cnt = 0

for i in range(N):
  while cnt and H[i] > 0:
    H[i] -= cnt + 1
    cnt = (cnt+1) % 4
    result += 1

  if H[i] <= 0:
    continue

  q, H[i] = divmod(H[i], 10)
  result += 4 * q

  while H[i] > 0:
    H[i] -= cnt + 1
    cnt = (cnt+1) % 4
    result += 1
print(result)