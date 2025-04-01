import sys

N, M = map(int, input().split())

no_hear = set()
result = set()

for _ in range(N):
    no_hear.add(sys.stdin.readline().rstrip())

for _ in range(M):
    no_watch = sys.stdin.readline().rstrip()
    if no_watch in no_hear:
        result.add(no_watch)
      
result = sorted(list(result))

print(len(result))
for no_hear_watch in result:
    print(no_hear_watch)