import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

N = int(input())
A = list(map(int, input().split()))
K = int(input())

def find_result(cur: str, depth: int) -> None:
	global result
	
	if cur and int(cur) > K:
		result = min(result, int(cur))
		return
	
	if depth > 10:
		return
	
	for num in A:
		find_result(cur + str(num), depth + 1)
		
result = float('inf')
find_result("", 0)
print(result)