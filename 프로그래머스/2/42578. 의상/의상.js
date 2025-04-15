function solution(clothes) {
    const clothMap = {};
    for(const [item, type] of clothes){
        if(!clothMap[type]) clothMap[type] = 0;
        clothMap[type] += 1;
    }
    
    let combinations = 1;
    for(const type in clothMap){
        combinations *= (clothMap[type] + 1);
    }
    
    return combinations - 1;
}