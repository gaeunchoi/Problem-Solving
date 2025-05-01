// 피보나치 문제였다 ... 오메 ...
function solution(n) {
    let a = 1, b = 2;
    for(let i = 2 ; i < n ; i++){
        [a, b] = [b, (a+b) % 1234567];
    }
    return n === 1 ? a : b;
}