def solution(x):
  return True if x % sum(list(map(int, str(x)))) == 0 else False