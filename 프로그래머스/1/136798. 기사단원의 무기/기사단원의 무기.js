function countDivisor(n){
    let cnt = 0;
    for(let i = 1 ; i <= Math.sqrt(n) ; i++){
        if(n % i === 0) cnt += (i === n / i) ? 1 : 2;  // 제곱수는 중복 방지
    }
    return cnt;
}

function solution(number, limit, power) {
    let result = 0;
    for(let i = 1 ; i <= +number ; i++){
        const divisor = countDivisor(i);
        result += divisor > limit ? power : divisor;
    }
    return result;
}