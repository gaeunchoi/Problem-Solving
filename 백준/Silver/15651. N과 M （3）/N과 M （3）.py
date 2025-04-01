import sys
import itertools

N, M = map(int, sys.stdin.readline().split())

# N을 1 ~ N까지 정수 배열로 바꿔주자
N = [i+1 for i in range(N)]



lists = list(itertools.product(N, repeat = M))

for value in lists:
    print(' '.join(map(str, value)))