function solution(a, b) {
    const day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'];
    const month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    
    return day[(month.slice(0, a-1).reduce((acc, cur) => acc + cur, 0) + b - 1) % 7]
}