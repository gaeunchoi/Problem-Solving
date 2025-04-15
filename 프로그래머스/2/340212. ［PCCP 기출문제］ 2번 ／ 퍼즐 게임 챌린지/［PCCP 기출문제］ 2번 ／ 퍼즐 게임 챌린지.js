function solution(diffs, times, limit) {
    const isPossible = (level) => {
        let totalTime = 0;
        const n = diffs.length;
        
        for(let i = 0 ; i < n ; i ++){
            const diff = diffs[i];
            const timeCur = times[i];
            const timePrev = i === 0 ? 0 : times[i-1];
            
            if(diff <= level) totalTime += timeCur;
            else {
                const mistake = diff - level;
                const retryTime = (timeCur + timePrev) * mistake;
                totalTime += retryTime + timeCur;
            }
            
            if(totalTime > limit) return false;
        }
        return true;
    }
    
    let left = 1;
    let right = 100000;
    let result = 0;
    
    while(left <= right){
        const mid = Math.floor((left + right) / 2);
        if(isPossible(mid)){
            result = mid;
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return result;
}