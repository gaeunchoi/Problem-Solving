from math import sqrt
def solution(n):
  v = sqrt(n)
  return (v+1)**2 if v == int(v) else -1