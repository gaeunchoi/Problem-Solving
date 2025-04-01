def solution(arr, queries):
  answer = []
  for s, e, k in queries:
    fArr = [i for i in arr[s:e+1] if i > k]
    answer.append(-1 if len(fArr) == 0 else min(fArr))
  return answer
