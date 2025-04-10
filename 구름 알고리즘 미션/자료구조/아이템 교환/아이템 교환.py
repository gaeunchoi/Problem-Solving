import sys
input = sys.stdin.readline

N, M = map(int, input().split())
gItem = set(input().split())
fItem = set(input().split())
for _ in range(M):
	a, b = input().split()
	
	if a in gItem and b in fItem:
		gItem.remove(a)
		fItem.remove(b)
		
		gItem.add(b)
		fItem.add(a)

for item in sorted(gItem):
	print(item, end = ' ')