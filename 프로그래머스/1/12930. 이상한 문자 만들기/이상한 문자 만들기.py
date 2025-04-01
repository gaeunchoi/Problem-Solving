def solution(s):
  s = s.lower()
  i = 0
  result = ''
  for v in s:
    if v == ' ':
      i = 0
      result += ' '
      continue
    
    if i % 2 == 0:
      result += v.upper()
    else:
      result += v.lower()
    
    i += 1
  
  return result

  