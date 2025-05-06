function solution(wants, number, discount) {
    let result = 0;
    for(let i = 0 ; i < discount.length - 9; i++){
        const window = discount.slice(i, i+10);
        const counter = {};
        
        for(const item of window){
            counter[item] = (counter[item] || 0) + 1
        }
        
        let success = true;
        for(let j = 0 ; j < wants.length ; j++){
            const want = wants[j];
            const num = number[j];
            
            if(!counter[want] || counter[want] < num){
                success = false;
                break;
            }
        }
        if(success) result++;
    }
    return result;
}