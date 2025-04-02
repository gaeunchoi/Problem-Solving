# 내림차순으로 정렬하고, 인용수가 논문수랑 같아지는 지점 체크(논문수 1부터 증가, idx 이용)
def solution(citations):
  answer = 0
  citations.sort(reverse=True)
  for cnt, citation in enumerate(citations):
    if citation >= cnt+1:
      answer = cnt+1
  return answer