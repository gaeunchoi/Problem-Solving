directions = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}

# x, y: 현재위치
x, y = map(int, input().split(" "))

N = int(input())
water= []
for _ in range(N):
  wx, wy = map(int, input().split(" "))
  water.append([wx, wy])

Q = int(input())
orders = list(map(str, input().split(" ")))

for order in orders:
  mx, my = x + directions[order][0], y + directions[order][1]
  if [mx, my] not in water:
    x, y = mx, my
  
print(x, y)
