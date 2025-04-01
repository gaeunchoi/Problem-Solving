attendance = [i for i in range(1, 31)]

for _ in range(28):
    apply = int(input())
    attendance.remove(apply)

print(min(attendance))
print(max(attendance))

