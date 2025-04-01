import sys

N = int(sys.stdin.readline())

texts = []
for _ in range(N):
    texts.append(sys.stdin.readline().rstrip())

texts = list(set(texts))

texts.sort()
texts.sort(key = len)

for i in range(len(texts)):
    print(texts[i])