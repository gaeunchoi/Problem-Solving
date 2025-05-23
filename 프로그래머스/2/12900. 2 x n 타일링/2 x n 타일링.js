function solution(n) {
    const MOD = 1000000007;
    let a = 1, b = 2;
    if(n === 1) return a;
    if(n === 2) return b;
       
    for(let i = 3; i <= n ; i++){
        [a, b] = [b, (a + b) % MOD];
    }
    return b;
}