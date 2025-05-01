function solution(arr) {
    const GCD = (a, b) => {
        while(b) {
            [a, b] = [b, a % b];    
        }
        return a;
    }
    
    const LCM = (a, b) => {
        return Math.floor((a * b) / GCD(a, b));
    }
    
    let result = arr[0];
    for(let i = 1 ; i < arr.length ; i++){
        result = LCM(result, arr[i]);
    }
    
    return result;
}