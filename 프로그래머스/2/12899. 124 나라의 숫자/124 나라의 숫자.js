function solution(n) {
    let result = '';
    while(n > 0){
        let m = n % 3;
        if(m === 0){
            result = '4' + result
            n = Math.floor(n / 3) - 1;
        } else {
            result = m + result;
            n = Math.floor( n / 3);
        }
    }
    return result
}