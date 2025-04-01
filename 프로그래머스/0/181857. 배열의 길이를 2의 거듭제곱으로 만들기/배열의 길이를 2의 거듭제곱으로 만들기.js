function solution(arr) {
  let i = 1;
  while(i < arr.length)
    i *= 2
  return [...arr, ... new Array(i - arr.length).fill(0)]
}