const solution = arr => {
  const rowLength = arr.length;
  const colLength = arr[0].length;

  if(rowLength > colLength){
    return arr.map(v => [...v, ...Array(rowLength - colLength).fill(0)])
  } else {
    for(let i = 0 ; i < colLength - rowLength ; i++){
      arr.push(Array(colLength).fill(0))
    }
  }

  return arr
}