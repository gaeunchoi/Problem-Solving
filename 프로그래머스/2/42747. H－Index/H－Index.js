function solution(citations) {
  var answer = 0;

  // 내림차순 정렬
  citations.sort((a, b) => b-a);

  [...citations].forEach((v, i) => {
    if(v >= i+1) answer = i+1
  });
  return answer;
}