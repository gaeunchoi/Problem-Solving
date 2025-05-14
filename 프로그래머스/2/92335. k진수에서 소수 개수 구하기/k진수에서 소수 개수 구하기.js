function isPrime(n){
    if(n <= 1) return false;
    if(n == 2) return true;
    if(n % 2 == 0) return false;
    
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
        if(cand.includes("0") || cand.length === 0) continue;
        if(isPrime(+cand)) result++;
    }
    return result;
}