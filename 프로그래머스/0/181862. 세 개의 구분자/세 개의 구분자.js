function solution(myStr) {
  let ans = myStr.split(/[a|b|c]/).filter(str => str)
  return ans.length ? ans : ["EMPTY"]
}