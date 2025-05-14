function isPrime(n){
    if (n < 2 || n % 2 === 0) return n === 2;
    for(let i = 3; i < Math.floor(n ** 0.5) + 1 ; i += 2){
        if(n % i == 0) return false;
    }
    return true;
}

function solution(n, k) {
    const convertNum = n.toString(k);
    const candidates = convertNum.split("0");
    
    let result = 0;
    for(const cand of candidates){
        if(isPrime(+cand)) result++;
    }
    return result;
}