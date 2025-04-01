function solution(price, money, count){
  let m = 0;
  for(let i = 1 ; i <= count ; i++){
    m += price*i
  }

  return money > m  ? 0 : m - money
}