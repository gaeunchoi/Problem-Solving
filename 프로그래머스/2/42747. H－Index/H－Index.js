function solution(citations) {
  var answer = 0;

  citations.sort((a, b) => b-a);

  [...citations].forEach((v, i) => {
    if(v >= i+1) answer = i+1
  });
  return answer;
}