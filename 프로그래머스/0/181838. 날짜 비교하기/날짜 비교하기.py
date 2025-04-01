def solution(date1, date2):
  y1, m1, d1 = date1
  y2, m2, d2 = date2
  if y1 < y2:
    return 1
  elif y1 > y2:
    return 0
  else:
    if m1 < m2:
      return 1
    elif m1 > m2:
      return 0
    else:
      if d1 < d2:
        return 1
      else:
        return 0