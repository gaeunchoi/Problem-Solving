function solution(my_strings, parts) {
  var answer = '';
  parts.forEach(([s, e], i) => answer += my_strings[i].slice(s, e+1))
  return answer;
}