function solution(arr) {
  let idx = 0
  let oldArr = arr
  while(true){
    const newArr = oldArr.map(ele => {
      if(ele >= 50 && ele % 2 === 0) return ele / 2
      if(ele < 50 && ele % 2 === 1) return 2 * ele + 1
      return ele
    })

    const isSame = oldArr.every((a, i) => a === newArr[i])
    if(isSame) break
    idx++

    oldArr= newArr
  }

  return idx
}