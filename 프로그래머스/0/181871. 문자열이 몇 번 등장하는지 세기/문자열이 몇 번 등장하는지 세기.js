function solution(myString, pat) {
  return [...myString].reduce((v, _, i) => myString.slice(i).startsWith(pat) ? v += 1 : v, 0)
}