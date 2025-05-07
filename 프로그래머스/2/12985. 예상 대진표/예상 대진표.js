const ceil = (num) => {
    return Math.ceil(num / 2);
}

function solution(n,a,b){
    let result = 1;
    
    while(ceil(a) !== ceil(b)){
        a = ceil(a);
        b = ceil(b);
        result++;
    }
    return result;
}