function solution(n, lost, reserve) {
    const notDupLost = lost.filter(x => !reserve.includes(x));
    const notDupReserve = reserve.filter(x => !lost.includes(x));
    notDupLost.sort((a, b) => a - b);
    notDupReserve.sort((a, b) => a - b);
    
    for(let extra of notDupReserve){
        const left = notDupLost.indexOf(extra-1);
        const right = notDupLost.indexOf(extra+1);
        
        if(left !== -1){
            notDupLost.splice(left, 1);
        } else if(right !== -1){
            notDupLost.splice(right, 1);
        }
    }
    
    return(n - notDupLost.length);
}