function solution(brown, yellow) {
    const total = brown + yellow;
    for(let h = 3 ; h < Math.floor(total ** 0.5) + 1; h++){
        if(total % h === 0){
            const w = Math.floor(total / h);
            if((w-2) * (h-2) === yellow) return [w, h]
        }
    }
}