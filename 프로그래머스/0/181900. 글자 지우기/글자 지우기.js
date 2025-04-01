function solution(my_string, indices) {
  var answer = Array.from(my_string);
  indices.sort((a, b) => b-a).forEach(v => {
    delete answer[v]
  })
  return answer.join("");
}