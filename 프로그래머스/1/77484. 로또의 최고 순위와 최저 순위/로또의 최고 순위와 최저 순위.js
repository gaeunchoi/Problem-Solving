function solution(lottos, win_nums) {
    let currentNums = lottos.filter(n => win_nums.includes(n));
    let zeroCnt = lottos.reduce((acc, cur) => cur === 0 ? acc + 1 : acc, 0);
    
    const minMatch = currentNums.length;
    const maxMatch = minMatch + zeroCnt;
    const getRank = cnt => cnt >= 2 ? 7 - cnt : 6;
    return [getRank(maxMatch), getRank(minMatch)];
}