function solution(storey) {
    let result = 0;
    
    while(storey !== 0){
        const res = storey % 10;
        if(5 < res){
            result += (10 - res);
            storey += 10;
        } else if(res < 5){
            result += res;
        } else {
            if(Math.floor(storey / 10) % 10 > 4) storey += 10
            result += res
        }
        storey = Math.floor(storey / 10);
    }
    
    return result;
}