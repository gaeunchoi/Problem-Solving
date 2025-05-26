function solution(msg) {
    let result = [];
    let alphaDict = {};
    let alphaDictLen = 0;
    
    for(let i = 1 ; i <= 26 ; i++){
        alphaDict[String.fromCharCode(64 + i)] = i;
        alphaDictLen++;
    }
    
    let s = 0, e = 0;
    while(true){
        e += 1
        if(e === msg.length){
            result.push(alphaDict[msg.slice(s, e)]);
            break;
        }
        
        if(!(msg.slice(s, e+1) in alphaDict)){
            alphaDict[msg.slice(s, e+1)] = ++alphaDictLen;
            result.push(alphaDict[msg.slice(s, e)]);   
            s = e;
        }
    }
    return result;
}