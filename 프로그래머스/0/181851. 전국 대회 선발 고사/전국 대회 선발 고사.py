def solution(rank, attendance):
  answer = 0
  result = []

  for i, score in enumerate(rank):
    if attendance[i]:
      result.append([score, i])
    
  result.sort(key = lambda x: x[0])
  return 10000*result[0][1] + 100*result[1][1] + result[2][1]