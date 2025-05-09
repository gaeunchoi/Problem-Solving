function solution(s) {
    const numbers = s.match(/\d+/g);
    
    const count = {};
    numbers.forEach((num) => {
        count[num] = (count[num] || 0) + 1;
    });
    
    const sorted = Object.entries(count).sort((a, b) => b[1] - a[1]);
    return sorted.map(([num]) => +num)
}