import sys
from math import gcd

N = int(input())
trees = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
dis_trees = []
for i in range(1, N):
    dis_trees.append(trees[i] - trees[i-1])

value = dis_trees[0]
for i in range(1, len(dis_trees)):
    value = gcd(value, dis_trees[i])

result = 0
for tree in dis_trees:
    result += tree // value - 1

print(result)