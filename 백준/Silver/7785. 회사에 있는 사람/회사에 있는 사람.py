n = int(input())
members = {}
for _ in range(n):
    name, status = input().split()
    members[name] = status

    if status == 'leave':
        del members[name]

result = sorted(members.items(), reverse=True)
result = dict(result)

for key in result.keys():
    print(key)