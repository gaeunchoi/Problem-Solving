function solution(n, t, m, p) {
    let fullString = "";
    let num = 0;
    
    while(fullString.length < t * m){
        fullString += (num++).toString(n).toUpperCase()
    }
    
    let result = "";
    for(let i = 0 ; i < t ; i++){
        result += fullString[i * m + (p-1)];
    }
    return result;
}