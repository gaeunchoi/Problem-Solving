function solution(sequence, k) {
    const N = sequence.length;
    let left = 0, total = 0;
    let result = [];
    let minLength = Infinity;
    
    for(let right = 0 ; right < N ; right++){
        total += sequence[right];
        
        while(total > k){
            total -= sequence[left]
            left += 1
        }
        
        if(total === k){
            if(right - left < minLength){
                minLength = right - left;
                result = [left, right];
            }
        }
    }
    
    return result;
}