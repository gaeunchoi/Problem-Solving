function solution(s) {
  return [...s].map((c, i) => {
    const nearIdx = s.slice(0, i).lastIndexOf(s[i])
    return nearIdx < 0 ? -1 : i - nearIdx
  })
}