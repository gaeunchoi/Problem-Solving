function solution(n, m) {
  const GCD = (a, b) => {
    while(b){
      [a, b] = [b, a%b]
    }
    return a
  }

  const LCM = (a, b) => {
    return (a*b) / GCD(a, b)
  }

  return [GCD(n, m), LCM(n, m)]
}