function solution(my_string) {
  let alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
  var answer = new Array(52).fill(0);
  for (let i = 0; i < my_string.length; i++) {
      answer[alp.indexOf(my_string[i])]++;
  }
  return answer;
}