function solution(strArr) {
  let ans = new Array(31).fill(0)
  strArr.forEach((ele) => {
    ans[ele.length]++
  })
  return Math.max(...ans)
}