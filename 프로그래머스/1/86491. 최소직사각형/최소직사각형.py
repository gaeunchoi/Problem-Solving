def solution(sizes):
  w, h = 0, 0
  for v1, v2 in sizes:
    short, long = min(v1, v2), max(v1, v2)
    w, h = max(w, short), max(h, long)

  return w*h