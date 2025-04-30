function solution(n) {
    const nOneCnt = n.toString(2).split("").filter(v => v === '1').length;
    let target = n+1;
    while(true){
        if(target.toString(2).split("").filter(v => v === '1').length === nOneCnt) return target;
        target++;
    }
}