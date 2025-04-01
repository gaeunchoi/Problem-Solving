def solution(numLog):
  answer = ''
  for idx in range(1, len(numLog)):
    value = numLog[idx] - numLog[idx-1]
    if value == 1:
      answer += 'w'
    elif value == -1:
      answer += 's'
    elif value == 10:
      answer += 'd'
    elif value == -10:
      answer += 'a'
  
  return answer