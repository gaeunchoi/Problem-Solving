function countPrimeNum(n){
    if(n < 2) return 0;
    
    let result = Array(n+1).fill(true);
    result[0] = false, result[1] = false;
    
    for(let i = 2 ; i < Math.floor(n ** 0.5) + 1; i++){
        if(result[i]){
            for(let j = i*i ; j <= n ; j += i){
                result[j] = false;
            }
        }
    }
    
    return result.reduce((acc, cur) => acc + Number(cur), 0);
    
}
function solution(n) {
    return countPrimeNum(n);
}