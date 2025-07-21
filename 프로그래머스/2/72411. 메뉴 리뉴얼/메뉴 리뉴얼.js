const getCombinations = (arr, selectNum) => {
    if(selectNum === 1) return arr.map((v) => [v]);
    const results = [];
    
    arr.forEach((v, i) => {
        const res = arr.slice(i+1);
        const combs = getCombinations(res, selectNum - 1);
        const attached = combs.map((comb) => [v, ...comb]);
        results.push(...attached)
    })
    return results;
}

function solution(orders, course) {
    let result = [];
    
    for(const cnt of course){
        const combinationsMap = new Map()
        for(const order of orders){
            const sortedOrder = order.split("").sort();
            const combs = getCombinations(sortedOrder, cnt);
            for(const comb of combs){
                const key = comb.join("");
                combinationsMap.set(key, (combinationsMap.get(key) || 0) + 1);
            }
        }
        
        let max = 0;
        for (const [key, val] of combinationsMap) {
            if (val >= 2) max = Math.max(max, val);
        }

        for (const [key, val] of combinationsMap) {
            if (val === max && val >= 2) result.push(key);
        }
    }
    
    return result.sort();
}